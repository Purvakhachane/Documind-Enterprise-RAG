import json
import os

REPORT_FILE = "reports/report.json"


def save_report(result):
    os.makedirs("reports", exist_ok=True)

    summary = result["summary"]

    report = {
        "pages": summary["pages"],
        "chunks": summary["chunks"],
        "file_size_kb": round(summary["file_size"] / 1024, 2),
        "status": "Success"
    }

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)
        