#!/usr/bin/env python3
"""
sam_concept_summarizer.py — Summarize any SAM concept.

Produces:
  * ELI5 summary (beginner friendly)
  * Technical summary (where it lives in UI, what table)
  * Key fields (mandatory/optional/critical)
  * Suggested next steps

Usage:
    python3 scripts/sam_concept_summarizer.py "asset lifecycle"
    python3 scripts/sam_concept_summarizer.py "software license"
    python3 scripts/sam_concept_summarizer.py "asset retirement"
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "opencode" / "guides" / "concept-summaries"
OUT.mkdir(parents=True, exist_ok=True)

CONCEPT_DB = {
    "asset lifecycle": {
        "eli5": (
            "An asset lifecycle is like the life of a laptop: someone asks for it, "
            "you buy it, it arrives, you give it to an employee, you fix it when "
            "it breaks, and eventually you replace it and recycle the old one."
        ),
        "technical": (
            "The asset lifecycle is tracked through the 'state' field on the "
            "alm_asset table. States typically include: In Stock, Ordered, "
            "Assigned, In Repair, Retired, and Disposed. Transitions between "
            "states can be controlled by business rules."
        ),
        "where": "Asset Management > Assets > All > State field",
        "table": "alm_asset",
        "terms": [
            {"term": "Asset Lifecycle", "def": "The journey from request to retirement"},
            {"term": "State", "def": "Current position in the lifecycle"},
            {"term": "Asset Tag", "def": "Unique physical identifier"},
        ],
        "next_steps": [
            "Create an asset and move it through all states",
            "Set up state transition rules",
            "Create a report showing assets by state",
        ],
    },
    "software license": {
        "eli5": (
            "A software license is like a permission slip that says how many copies "
            "of a program your company is allowed to use. If you have 50 licenses "
            "but 60 people using the software, you're breaking the rules."
        ),
        "technical": (
            "Software licenses are tracked in the alm_software table with fields "
            "for license count, installation count, license type, and expiration "
            "date. License reconciliation compares installations to entitlements."
        ),
        "where": "Asset Management > Software > All",
        "table": "alm_software",
        "terms": [
            {"term": "License Count", "def": "How many copies you're allowed to use"},
            {"term": "Installation Count", "def": "How many copies are actually installed"},
            {"term": "Compliance", "def": "Installation count <= License count"},
        ],
        "next_steps": [
            "Create a software license record",
            "Run license reconciliation",
            "Identify over-licensed and under-licensed software",
        ],
    },
    "asset retirement": {
        "eli5": (
            "Asset retirement is when you decide an asset is too old or broken to "
            "keep using. You wipe its data, mark it as retired in ServiceNow, and "
            "either recycle it, donate it, or return it to the vendor."
        ),
        "technical": (
            "Asset retirement sets the alm_asset state to 'Retired' and records "
            "the retirement date and disposal method. The asset remains in the "
            "database for historical reporting but is no longer active."
        ),
        "where": "Asset Management > Assets > All > State = Retired",
        "table": "alm_asset",
        "terms": [
            {"term": "Retirement Date", "def": "When the asset was taken out of service"},
            {"term": "Disposal Method", "def": "How it was disposed (recycle, donate, return)"},
        ],
        "next_steps": [
            "Retire an old asset",
            "Create a retirement report",
            "Set up automatic retirement alerts",
        ],
    },
    "asset tag": {
        "eli5": (
            "An asset tag is like a name sticker on a lunchbox. It's a unique "
            "number (like AST-001234) that you stick on each physical asset so "
            "you can match it to its record in ServiceNow."
        ),
        "technical": (
            "The asset tag is stored in the asset_tag field on alm_asset. It "
            "should be unique across all assets and is often used for barcode "
            "scanning during audits."
        ),
        "where": "Asset Management > Assets > All > Asset Tag field",
        "table": "alm_asset",
        "terms": [
            {"term": "Asset Tag", "def": "Unique identifier sticker on physical asset"},
            {"term": "Barcode", "def": "Machine-readable version of asset tag"},
        ],
        "next_steps": [
            "Define an asset tag numbering format",
            "Create assets with asset tags",
            "Scan assets during inventory audit",
        ],
    },
    "vendor": {
        "eli5": (
            "A vendor is the company you buy assets from — like Dell, Apple, "
            "Microsoft, or your local IT supplier. You need vendor records so "
            "ServiceNow knows who to call for support or warranty claims."
        ),
        "technical": (
            "Vendors are stored in the alm_vendor table. Each vendor record "
            "includes contact information and can be linked to assets, "
            "contracts, and purchase orders."
        ),
        "where": "Asset Management > Vendors > All",
        "table": "alm_vendor",
        "terms": [
            {"term": "Vendor", "def": "Company that sells or supports assets"},
            {"term": "Vendor Contact", "def": "Person to contact at the vendor"},
        ],
        "next_steps": [
            "Create vendor records for all suppliers",
            "Link assets to their vendors",
            "Track warranty expiration by vendor",
        ],
    },
}

TERM_ALIASES = {
    "assetlifecycle": "asset lifecycle",
    "asset_lifecycle": "asset lifecycle",
    "softwarelicense": "software license",
    "software_license": "software license",
    "assetretirement": "asset retirement",
    "asset_retirement": "asset retirement",
    "assettag": "asset tag",
    "asset_tag": "asset tag",
}


def normalize(concept: str) -> str:
    c = concept.strip().lower()
    return TERM_ALIASES.get(c, c)


def summarize(concept: str) -> dict:
    key = normalize(concept)
    if key not in CONCEPT_DB:
        return {
            "concept": concept,
            "found": False,
            "message": (
                f"Concept '{concept}' not in built-in database. "
                f"Known concepts: {', '.join(sorted(CONCEPT_DB.keys()))}"
            ),
        }
    data = CONCEPT_DB[key]
    return {
        "concept": concept,
        "key": key,
        "found": True,
        "eli5": data["eli5"],
        "technical": data["technical"],
        "where": data["where"],
        "table": data.get("table", ""),
        "terms": data["terms"],
        "next_steps": data["next_steps"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def render_md(summary: dict) -> str:
    if not summary["found"]:
        return f"# Concept Not Found\n\n{summary['message']}\n"
    lines = [
        f"# {summary['concept'].title()} — SAM Concept Summary",
        "",
        f"*Generated: {summary['generated_at']}*",
        f"*Table: {summary['table']}*",
        "",
        "## ELI5 (Explain Like I'm 5)",
        "",
        summary["eli5"],
        "",
        "## Technical Detail",
        "",
        summary["technical"],
        "",
        "## Where to Find It in ServiceNow",
        "",
        summary["where"],
        "",
        "## Key Terminology",
        "",
        "| Term | Definition |",
        "|------|------------|",
    ]
    for t in summary["terms"]:
        lines.append(f"| {t['term']} | {t['def']} |")
    lines += ["", "## Suggested Next Steps", ""]
    for i, step in enumerate(summary["next_steps"], 1):
        lines.append(f"{i}. {step}")
    lines += ["", "---", ""]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 sn_concept_summarizer.py '<concept>'")
        print(f"Known concepts: {', '.join(sorted(CONCEPT_DB.keys()))}")
        sys.exit(1)

    concept = " ".join(sys.argv[1:])
    summary = summarize(concept)
    md = render_md(summary)

    safe_name = concept.strip().lower().replace(" ", "_").replace("/", "-")
    out_path = OUT / f"{safe_name}.md"
    out_path.write_text(md, encoding="utf-8")

    print(md)
    print(f"\n--- Saved to {out_path} ---")


if __name__ == "__main__":
    main()
