"""Check local Lean sources against an explicit, read-only pinned package cache.

Run this script inside the repository's required resource-cap wrapper.
No Lake update, cache download, or source-corpus write is performed.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
from axiom_guard import check_axiom_output

parser = argparse.ArgumentParser()
parser.add_argument("--packages", type=Path, required=True)
parser.add_argument("--log", type=Path)
parser.add_argument("files", nargs="+")
args = parser.parse_args()
manifest = json.loads((args.packages.parent.parent / "lake-manifest.json").read_text())
mathlib = next(p for p in manifest["packages"] if p["name"] == "mathlib")
assert mathlib["rev"] == "c5ea00351c28e24afc9f0f84379aa41082b1188f"
locked = json.loads(Path(__file__).with_name("dependencies.lock.json").read_text())
assert {p["name"]: p["rev"] for p in manifest["packages"]} == {
    p["name"]: p["rev"] for p in locked["packages"]}
head = subprocess.check_output(["git", "-C", str(args.packages / "mathlib"),
    "rev-parse", "HEAD"], text=True).strip()
assert head == mathlib["rev"]
version = subprocess.check_output(["lean", "--version"], text=True)
assert "version 4.30.0," in version and "d024af099ca4bf2c86f649261ebf59565dc8c622" in version
print(version.strip(), flush=True)
print("mathlib " + mathlib["rev"], flush=True)
log = [version.strip(), "mathlib " + mathlib["rev"]]
env = os.environ.copy()
env["LEAN_PATH"] = os.pathsep.join(str(p / ".lake/build/lib/lean")
    for p in args.packages.iterdir() if p.is_dir())
for file in args.files:
    print("CHECK " + file, flush=True)
    # The enclosing Windows job caps committed memory. Lean's internal -M
    # additionally counts mapped imports and can reject a cache below that cap.
    result = subprocess.run(["lean", "-j1", file], env=env,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8")
    print(result.stdout, end="", flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    count = check_axiom_output(Path(file).read_text(encoding="utf-8"), result.stdout)
    message = f"PASS {count} dependency closures: allowed foundations only"
    print(message, flush=True)
    log.extend(["CHECK " + Path(file).name, result.stdout.rstrip(), message, "EXIT 0"])
if args.log:
    args.log.write_text("\n".join(log) + "\n", encoding="utf-8", newline="\n")
