"""Strict, portable integrity checks for a frozen publication directory."""
from pathlib import Path, PurePosixPath
import hashlib
import re


def write_manifest(root: Path, files):
    lines = [hashlib.sha256((root / name).read_bytes()).hexdigest() + '  ' + name
             for name in files]
    (root / 'SHA256SUMS.txt').write_text('\n'.join(lines) + '\n',
                                      encoding='utf-8', newline='\n')


def verify_manifest(root: Path, files):
    raw = (root / 'SHA256SUMS.txt').read_bytes()
    assert b'\r' not in raw and raw.endswith(b'\n'), 'Manifest must use LF with final newline'
    entries = {}
    for line in raw.decode('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match, 'Malformed checksum line'
        sha, name = match.groups()
        path = PurePosixPath(name)
        assert not path.is_absolute() and '..' not in path.parts and '\\' not in name
        assert name not in entries, 'Duplicate checksum entry'
        entries[name] = sha
    assert set(entries) == set(files), 'Manifest differs from public allowlist'
    for name, sha in entries.items():
        path = root / name
        assert not path.is_symlink() and path.is_file(), 'Missing or linked file: ' + name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == sha, 'Checksum mismatch: ' + name
    actual = set()
    for path in root.rglob('*'):
        if '.git' in path.parts:
            continue
        assert not path.is_symlink(), 'Linked entry in frozen export'
        if path.is_file():
            actual.add(path.relative_to(root).as_posix())
    assert actual == set(files) | {'SHA256SUMS.txt'}, 'Non-allowlisted or missing export files'
