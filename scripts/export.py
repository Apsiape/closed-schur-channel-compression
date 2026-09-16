"""Produce an allowlisted clean candidate without modifying any research source."""
from pathlib import Path
import datetime
import shutil
import subprocess
import sys
import zipfile
sys.dont_write_bytecode = True
from public_files import FILES
from package_manifest import write_manifest, verify_manifest

root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, '-B', str(root/'scripts/verify.py')],check=True)
stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
target=root/'public-export'/('closed-schur-channel-compression-'+stamp)
target.mkdir(parents=True,exist_ok=False)
for relative in FILES:
    src=root/relative; dst=target/relative
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(src,dst)
write_manifest(target, FILES)
subprocess.run([sys.executable,'-B',str(target/'scripts/verify.py')],check=True)
verify_manifest(target, FILES)
archive=target.with_suffix('.zip')
with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as package:
    for relative in (*FILES, 'SHA256SUMS.txt'):
        package.write(target/relative, arcname=relative)
with zipfile.ZipFile(archive) as package:
    assert set(package.namelist()) == set(FILES) | {'SHA256SUMS.txt'}
    assert package.testzip() is None
    for relative in package.namelist():
        assert package.read(relative) == (target/relative).read_bytes(), relative
print('Clean candidate:',target)
print('Manifest-only ZIP:',archive)
print('No commit, remote, release or publication created.')
