"""Regression tests for checksum portability and strict export boundaries."""
from pathlib import Path
import sys
import tempfile

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from package_manifest import write_manifest, verify_manifest

with tempfile.TemporaryDirectory(prefix='schur-package-check-') as temporary:
    root = Path(temporary)
    (root / 'sample.txt').write_bytes(b'publication sample\n')
    files = ('sample.txt',)
    write_manifest(root, files)
    verify_manifest(root, files)
    manifest = root / 'SHA256SUMS.txt'
    clean = manifest.read_bytes()

    def rejected():
        try:
            verify_manifest(root, files)
        except AssertionError:
            return
        raise AssertionError('Invalid export was accepted')

    for invalid in (clean.replace(b'\n', b'\r\n'), clean + clean, clean.rstrip(b'\n')):
        manifest.write_bytes(invalid)
        rejected()
    manifest.write_bytes(clean)
    for directory in ('build', '__pycache__', 'tmp'):
        (root / directory).mkdir()
        stray = root / directory / 'stray.bin'
        stray.write_bytes(b'not publication material')
        rejected()
        stray.unlink()
    (root / 'sample.txt').write_bytes(b'changed\n')
    rejected()
print('PASS: valid LF export; rejects CRLF, duplicates, missing newline, hidden build/cache files and changed bytes')
