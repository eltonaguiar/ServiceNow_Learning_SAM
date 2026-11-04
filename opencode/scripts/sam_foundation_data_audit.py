#!/usr/bin/env python3
"""
sam_foundation_data_audit.py — Audit SAM foundation data completeness.

Checks whether the required foundation data exists before assets can be
managed effectively.

Usage:
    python3 scripts/sam_foundation_data_audit.py
    python3 scripts/sam_foundation_data_audit.py --format json
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "opencode" / "guides" / "foundation-data-audit"
OUT.mkdir(parents=True, exist_ok=True)

# Foundation data items that should exist before asset management works.
FOUNDATION_DATA = {
    "Companies": {
        "table": "cmn_company",
        "critical": True,
        "description": "Companies you buy from or work with",
        "examples": ["Dell Technologies", "Microsoft", "CDW", "SHI"],
    },
    "Vendors": {
        "table": "cmn_vendor_company",
        "critical": True,
        "description": "Approved vendors for purchasing assets",
        "examples": ["Dell Technologies", "Insight Global", "CDW"],
    },
    "Locations": {
        "table": "cmn_location",
        "critical": True,
        "description": "Offices, warehouses, data centers where assets live",
        "examples": ["New York HQ", "London Office", "Chicago Warehouse"],
    },
    "Departments": {
        "table": "cmn_department",
        "critical": True,
        "description": "Internal departments that own assets",
        "examples": ["IT", "Finance", "HR", "Marketing"],
    },
    "Cost Centers": {
        "table": "cmn_cost_center",
        "critical": False,
        "description": "Budget centers for cost accountability",
        "examples": ["IT-Operations", "Finance-Systems"],
    },
    "Asset Categories": {
        "table": "alm_asset_category",
        "critical": True,
        "description": "Types of assets (determines form fields)",
        "examples": ["Laptop", "Server", "Software License", "Monitor"],
    },
    "Asset States": {
        "table": "alm_asset_state",
        "critical": True,
        "description": "Lifecycle stages an asset can be in",
        "examples": ["In Stock", "Ordered", "Assigned", "In Repair", "Retired"],
    },
    "Asset Models": {
        "table": "alm_asset_model",
        "critical": False,
        "description": "Specific make and model of hardware assets",
        "examples": ["Dell XPS 13", "MacBook Pro 14\"", "iPhone 15"],
    },
    "Users": {
        "table": "sys_user",
        "critical": True,
        "description": "Employees who are assigned assets",
        "examples": ["Sarah Jenkins", "Mike Chen"],
    },
}

def audit() -> dict:
    results = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_items": len(FOUNDATION_DATA),
        "critical_items": sum(1 for v in FOUNDATION_DATA.values() if v["critical"]),
        "audit": [],
    }

    for name, info in FOUNDATION_DATA.items():
        entry = {
            "item": name,
            "table": info["table"],
            "critical": info["critical"],
            "description": info["description"],
            "examples": info["examples"],
            "status": "unknown",  # In a real deployment, query ServiceNow
            "notes": "Check this table in your ServiceNow instance",
        }
        results["audit"].append(entry)

    # Sort: critical first, then alphabetical
    results["audit"].sort(key=lambda x: (not x["critical"], x["item"]))
    return results

def render_md(audit_result: dict) -> str:
    lines = [
        "# SAM Foundation Data Audit",
        "",
        f"*Generated: {audit_result['generated_at']}*",
        "",
        "## Summary",
        "",
        f"- Total foundation data areas: {audit_result['total_items']}",
        f"- Critical (must have): {audit_result['critical_items']}",
        "",
        "## Audit Checklist",
        "",
        "| Item | Table | Critical | Description | Status |",
        "|------|-------|----------|-------------|--------|",
    ]
    for item in audit_result["audit"]:
        crit = "**CRITICAL**" if item["critical"] else "Optional"
        lines.append(
            f"| {item['item']} | {item['table']} | {crit} | "
            f"{item['description']} | {item['status']} |"
        )

    lines += ["", "## Examples by Category", ""]
    for item in audit_result["audit"]:
        examples = ", ".join(item["examples"])
        lines.append(f"- **{item['item']}**: {examples}")

    lines += ["", "## Next Steps", ""]
    lines.append("1. Log into your ServiceNow instance")
    lines.append("2. Navigate to each table listed above")
    "3. Verify records exist for your organization"
    lines.append("3. Create any missing foundation data")
    lines.append("4. Only then create asset records")

    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(description="Audit SAM foundation data")
    ap.add_argument("--format", choices=["md", "json"], default="md")
    args = ap.parse_args()

    result = audit()

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(render_md(result))

    out_path = OUT / "foundation-data-audit.md"
    out_path.write_text(render_md(result), encoding="utf-8")
    print(f"\n--- Saved to {out_path} ---")

if __name__ == "__main__":
    main()
