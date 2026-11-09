"""Behavioral checks of location boundaries; Gemini is mocked only in these tests."""
import copy
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pickup", ROOT / "starter-code/pickup_checkin.py")
pickup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pickup)


@pytest.fixture
def catalog():
    return json.loads((ROOT / "data/pickup_catalog.json").read_text())


def draft(point_id="P_REAR", action="propose_pickup"):
    return {"draft_tag": pickup.TAG, "action": action, "pickup_point_id": point_id,
            "question": "Bạn xác nhận cổng sau, Đường B, cùng phía hiệu thuốc LAB đúng không?",
            "reason": "Mô tả khớp điểm trong danh mục.", "requires_confirmation": True}


def proposal(catalog, payload=None):
    return {"catalog_version": catalog["version"], "place_id": catalog["place_id"],
            "model_output": payload or draft(), "status": "pending_confirmation"}


@pytest.mark.parametrize("point_id", ["P_MAIN", "P_REAR", "P_SIDE_E", "P_SIDE_W"])
def test_verified_open_accessible_point_can_be_proposed(catalog, point_id):
    pickup.validate_response(draft(point_id), catalog)


@pytest.mark.parametrize("point_id", ["INVENTED", "P_SERVICE", None])
def test_unknown_or_closed_point_is_rejected(catalog, point_id):
    with pytest.raises(pickup.PickupError):
        pickup.validate_response(draft(point_id), catalog)


@pytest.mark.parametrize("field,value", [
    ("requires_confirmation", False), ("requires_confirmation", "true"),
    ("action", "confirmed"), ("draft_tag", ""), ("question", ""),
])
def test_model_cannot_bypass_confirmation_or_schema(catalog, field, value):
    payload = draft()
    payload[field] = value
    with pytest.raises(pickup.PickupError):
        pickup.validate_response(payload, catalog)


def test_model_generated_coordinates_are_rejected(catalog):
    payload = draft()
    payload["coordinates"] = {"lat": 99, "lon": 99}
    with pytest.raises(pickup.PickupError):
        pickup.validate_response(payload, catalog)


def test_clarification_must_not_silently_select_gate(catalog):
    pickup.validate_response(draft(None, "ask_clarification"), catalog)
    with pytest.raises(pickup.PickupError):
        pickup.validate_response(draft("P_REAR", "ask_clarification"), catalog)


@pytest.mark.parametrize("passenger,driver", [(False, True), (True, False), (False, False)])
def test_no_finalized_coordinates_without_both_confirmations(catalog, passenger, driver):
    result = pickup.confirm_pickup(proposal(catalog), catalog,
                                   passenger_confirmed=passenger, driver_acknowledged=driver)
    assert result == {"status": "pending_confirmation", "coordinates": None}


def test_confirmation_uses_catalog_coordinates_exactly(catalog):
    result = pickup.confirm_pickup(proposal(catalog), catalog,
                                   passenger_confirmed=True, driver_acknowledged=True)
    expected = next(p for p in catalog["points"] if p["id"] == "P_REAR")
    assert result["coordinates"] == expected["coordinates"]
    assert result["side"] == expected["side"]


@pytest.mark.parametrize("change", ["version", "closed", "vehicle", "unverified", "stale"])
def test_recheck_catalog_at_confirmation_time(catalog, change):
    proposed = proposal(catalog)
    updated = copy.deepcopy(catalog)
    rear = next(p for p in updated["points"] if p["id"] == "P_REAR")
    if change == "version":
        updated["version"] = "lab-v2"
    elif change == "closed":
        rear["open"] = False
    elif change == "vehicle":
        rear["vehicle_types"] = ["bike"]
    elif change == "unverified":
        rear["verified"] = False
    else:
        updated["is_fresh"] = False
    with pytest.raises(pickup.PickupError):
        pickup.confirm_pickup(proposed, updated, passenger_confirmed=True, driver_acknowledged=True)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), True, 91, "0.001"])
def test_bad_coordinates_cannot_enter_catalog(catalog, value):
    catalog["points"][0]["coordinates"]["lat"] = value
    with pytest.raises(pickup.PickupError):
        pickup.validate_catalog(catalog)


def test_gemini_contract_and_backend_preview(monkeypatch, tmp_path, catalog):
    from google import genai
    monkeypatch.setattr(pickup, "ROOT", tmp_path)
    monkeypatch.setenv("GEMINI_API_KEY", "offline-test-placeholder")
    client = MagicMock()
    generate = client.__enter__.return_value.models.generate_content
    generate.return_value = SimpleNamespace(text=json.dumps(draft()))
    monkeypatch.setattr(genai, "Client", MagicMock(return_value=client))
    result = pickup.evaluate_pickup("Cổng sau cạnh hiệu thuốc LAB", catalog)
    assert result["status"] == "pending_confirmation"
    assert result["point_preview"]["street"] == "Đường B (mô phỏng)"
    assert "coordinates" not in result["point_preview"]
    config = generate.call_args.kwargs["config"]
    assert config.system_instruction == pickup.SYSTEM_PROMPT
    assert config.response_mime_type == "application/json"


def test_missing_key_cannot_be_reported_as_model_success(monkeypatch, tmp_path, catalog):
    monkeypatch.setattr(pickup, "ROOT", tmp_path)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        pickup.evaluate_pickup("Cổng sau", catalog)
