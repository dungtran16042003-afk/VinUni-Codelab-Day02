"""Reproduce the hypothetical spreadsheet scenario; not measured business results."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def calculate(a):
    saved_seconds = a["baseline_location_seconds"] - a["target_location_seconds"]
    hours_month = a["affected_trips_per_day"] * a["days_per_month"] * saved_seconds / 3600
    fewer_cancels = a["affected_trips_per_day"] * (
        a["baseline_location_cancellation_rate"] - a["target_location_cancellation_rate"]
    )
    return {
        "status": a["status"],
        "seconds_saved_per_affected_trip": saved_seconds,
        "location_time_reduction_percent": round(saved_seconds / a["baseline_location_seconds"] * 100, 2),
        "driver_hours_freed_per_month": hours_month,
        "opportunity_time_value_vnd_per_month": hours_month * a["time_value_vnd_per_hour"],
        "fewer_location_cancellations_per_day": round(fewer_cancels, 6),
        "additional_completed_trips_per_day": round(fewer_cancels * a["recovered_trips_completed_rate"], 6),
        "additional_gross_fares_vnd_per_month": round(fewer_cancels * a["recovered_trips_completed_rate"] * a["days_per_month"] * a["average_fare_vnd"]),
        "first_gate_correct_improvement_percentage_points": round((a["target_first_gate_correct_rate"] - a["baseline_first_gate_correct_rate"]) * 100, 2),
        "platform_net_revenue": "unknown: requires actual retained share and costs",
        "interpretation": "Time value is not cash savings. Gross fares are not platform net revenue. Do not sum these figures as profit or ROI."
    }


if __name__ == "__main__":
    assumptions = json.loads((ROOT / "data/impact_assumptions.json").read_text())
    result = calculate(assumptions)
    output = ROOT / "artifacts/impact-scenario.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
