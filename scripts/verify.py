"""Offline, bounded public-package integrity checks; not theorem certification."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys
sys.dont_write_bytecode = True
from pypdf import PdfReader
from public_files import FILES
from package_manifest import verify_manifest
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--rebuilt',type=Path)
args=p.parse_args()
assert len(FILES)==len(set(FILES))
for name in FILES:
    path=root/name
    assert path.is_file(), 'Missing '+name
    assert path.stat().st_size < 3*1024*1024, 'Unexpectedly large '+name
    if path.suffix in {'.md','.tex','.bib','.json','.cff','.py','.lean','.txt'}:
        body=path.read_text(encoding='utf-8-sig')
        assert not re.search(r'(?<![A-Za-z])[A-Za-z]:(?:/(?!/)|\\[^\s\\{}]+\\)',body), 'Local path '+name
        if path.suffix != '.py':
            assert not any(x in body for x in ['\ue200','\ue201','[INSERT','TODO:']), 'Placeholder '+name
        assert all(line.rstrip()==line for line in body.splitlines()), 'Trailing whitespace '+name
source=(root/'paper/manuscript.md').read_text(encoding='utf-8')
tex=(root/'paper/manuscript.tex').read_text(encoding='utf-8')
bib=(root/'paper/references.bib').read_text(encoding='utf-8')
assert source.count('## Theorem ')==5
assert source.count('## Lemma ')==2
assert source.count('## Corollary ')==1
for word in ['AI assistance','Seth Douglas','seth.douglas@gmail.com',
             'mandatory','purifier','no-flush','T^{-4}']:
    assert word in source, word
for token in ['\\tag{2.9}', '\\tag{3.9}', '\\tag{6.18}', '\\tag{9.7}']:
    assert token in tex, token
keys=set(re.findall(r'@\w+\{([^,]+),',bib))
cited=set()
for group in re.findall(r'\\cite[pt]?(?:\[[^\]]*\])*\{([^}]+)\}',tex):
    cited.update(key.strip() for key in group.split(','))
assert cited==keys, ('citation mismatch',cited^keys)
assert len(keys)>0
meta=(root/'CITATION.cff').read_text()
assert 'Seth' in meta and 'seth.douglas@gmail.com' in meta
assert meta.count('doi: 10.5281/zenodo.22785669') == 2
assert 'repository-code: https://github.com/Apsiape/closed-schur-channel-compression' in meta
assert 'independent researcher' not in source.lower()
reader=PdfReader(root/'output/pdf/manuscript.pdf')
assert 15<=len(reader.pages)<=40
assert reader.metadata.author=='Seth Douglas'
pages=[page.extract_text() for page in reader.pages]
full='\n'.join(pages)
for phrase in ['AI assistance','References','Theorem 8','Lemma 6']:
    assert phrase in full, phrase
assert not re.search(r'\[\?\]|\?\?',full)
if args.rebuilt:
    rebuilt=PdfReader(args.rebuilt)
    assert [page.extract_text() for page in rebuilt.pages]==pages,'PDF page text differs'
    print('PASS rebuilt PDF has identical extracted page text')
manifest=root/'SHA256SUMS.txt'
if manifest.exists():
    verify_manifest(root, FILES)
    print('PASS clean-export hashes and exact file set')
prov=json.loads((root/'SOURCE-MAP.json').read_text())
for item in prov['copied_code']:
    assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256']
print('PASS',len(FILES),'public files;',len(pages),'PDF pages;',len(keys),'citations; author, scoped metadata and provenance')
print('These checks do not establish mathematical correctness, layout quality or novelty.')
