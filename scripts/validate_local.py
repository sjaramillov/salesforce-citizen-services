#!/usr/bin/env python3
"""Offline format and contract-reference checks; never calls a tenant or runtime."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
RESULTS: list[dict] = []


def record(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": passed, "detail": detail})


def all_nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from all_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from all_nodes(child)


def resolve_pointer(document, reference: str) -> None:
    if not reference.startswith("#/"):
        raise ValueError("Only internal JSON-pointer references are supported")
    node = document
    for part in reference[2:].split("/"):
        key = part.replace("~1", "/").replace("~0", "~")
        node = node[int(key)] if isinstance(node, list) else node[key]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'artifacts/local-validation.json')
    args = parser.parse_args()
    try:
        import yaml
    except ImportError:
        record("dependency:PyYAML", False, "Missing PyYAML; no installation attempted")
        yaml = None

    excluded = {'.git', '.venv', 'node_modules', 'artifacts', '__pycache__', '.sf', '.sfdx', '.terraform', 'target'}
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and not excluded.intersection(p.relative_to(ROOT).parts))
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("docs/evidence/") or rel.startswith("docs/provenance/"):
            continue
        if path.suffix in {".xml", ".json", ".yaml", ".yml"}:
            try:
                if path.suffix == ".xml":
                    ET.parse(path)
                elif path.suffix == ".json":
                    json.loads(path.read_text())
                elif yaml:
                    document = yaml.safe_load(path.read_text())
                    if rel.endswith(".openapi.yaml"):
                        assert str(document.get("openapi", "")).startswith("3."), "OpenAPI 3 expected"
                        assert document["info"]["title"] and document["info"]["version"]
                        assert document["paths"], "At least one path expected"
                        references = [node["$ref"] for node in all_nodes(document) if "$ref" in node]
                        for reference in references:
                            resolve_pointer(document, reference)
                        operation_ids = []
                        for route, item in document["paths"].items():
                            assert route.startswith("/"), "Path must start with slash"
                            for method, operation in item.items():
                                if method not in {"get", "post", "put", "patch", "delete", "head", "options", "trace"}:
                                    continue
                                assert operation.get("responses"), "Operation needs responses"
                                if "operationId" in operation:
                                    operation_ids.append(operation["operationId"])
                        assert len(operation_ids) == len(set(operation_ids)), "Duplicate operationId"
                        record(f"contract:{rel}", True, f"Minimal structure and {len(references)} internal references resolved; not full OpenAPI schema validation")
                else:
                    continue
                record(f"format:{rel}", True, "Parsed locally; runtime and provider schema not checked")
            except Exception as exc:
                record(f"format:{rel}", False, f"{type(exc).__name__}: {exc}")

    component = ROOT / "force-app/main/default/lwc/cscBenefitPortal"
    js = (component / "cscBenefitPortal.js").read_text()
    html = (component / "cscBenefitPortal.html").read_text()
    handlers = re.findall(r"on\w+=\{(\w+)\}", html)
    record("lwc:handlers", all(re.search(rf"\b{re.escape(name)}\s*\(", js) for name in handlers), f"{len(handlers)} template handlers have methods; no compilation performed")
    record("lwc:demo-notice", "Demostración con datos ficticios" in html, "Visible illustrative-only disclosure")
    record("lwc:local-data", "fetch(" not in js and "@salesforce/apex" not in js, "No direct HTTP/Apex call in selected component")

    agent = (ROOT / "salesforce/agentforce/benefit-agent.reference.agent").read_text()
    case_ids = set(re.findall(r"BEN-\d{4}-\d{6}", agent))
    record("agent:sample-scope", case_ids == {"BEN-2026-004219", "BEN-2026-004227"}, f"{len(case_ids)} unique fictional case IDs; no AgentScript grammar validation")

    # Narrow safeguard for selected text; this is not a full secret/history scanner.
    sensitive = re.compile(r"\b(?:00D|005|00G)[A-Za-z0-9]{12,15}\b|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bAKIA[0-9A-Z]{16}\b|https?://[^\s<>\"']*\.(?:my\.salesforce\.com|my\.site\.com|salesforce-experience\.com)")
    matches = []
    for path in files:
        if path.suffix not in {".md", ".json", ".xml", ".yaml", ".js", ".html", ".css", ".agent", ".sql"}:
            continue
        if sensitive.search(path.read_text()):
            matches.append(path.relative_to(ROOT).as_posix())
    record("selected-text:tenant-secret-patterns", not matches, "No narrow pattern matches" if not matches else "Review paths: " + ", ".join(matches))

    report = {
        "checkedAtUtc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "pyyaml": getattr(yaml, "__version__", None),
        "scope": "Offline parsing, minimal OpenAPI structure/internal refs, selected source consistency. No LWC compilation, AgentScript compilation, MUnit, Salesforce, Mule, SQL, network or UI execution.",
        "results": RESULTS,
        "passed": all(item["passed"] for item in RESULTS),
    }
    target = args.output
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"{sum(x['passed'] for x in RESULTS)}/{len(RESULTS)} checks passed; report: {target.relative_to(ROOT) if target.is_relative_to(ROOT) else target.name}")
    for result in RESULTS:
        if not result["passed"]:
            print(f"FAIL {result['name']}: {result['detail']}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
