"""Validate each requested Lean dependency closure against allowed foundations."""
import re

ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def check_axiom_output(source, output):
    queries = re.findall(r"^\s*#print\s+axioms\s+(\S+)", source, re.MULTILINE)
    if not queries or len(queries) != len(set(queries)):
        raise ValueError("Expected distinct #print axioms declarations")
    if re.search(r"^\s*(?:private\s+)?axiom\s", source, re.MULTILINE):
        raise ValueError("Local scientific axiom declaration")
    if "sorryAx" in output or "declaration uses `sorry`" in output:
        raise ValueError("Lean admission detected")
    rows = re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", output)
    rows += [(name, "") for name in re.findall(
        r"'([^']+)' does not depend on any axioms", output)]
    seen = set()
    for name, raw in rows:
        candidates = [q for q in queries if name == q or name.endswith("." + q)]
        if len(candidates) != 1 or candidates[0] in seen:
            raise ValueError("Unexpected or duplicate dependency report: " + name)
        seen.add(candidates[0])
        axioms = {x.strip() for x in raw.split(",") if x.strip()}
        if not axioms <= ALLOWED_AXIOMS:
            raise ValueError("Unexpected axioms: " + ", ".join(sorted(axioms - ALLOWED_AXIOMS)))
    if seen != set(queries):
        raise ValueError("Missing dependency reports: " + ", ".join(sorted(set(queries) - seen)))
    return len(seen)
