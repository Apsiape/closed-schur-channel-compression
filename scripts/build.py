"""Portable manuscript build; no install/network, source PDF never overwritten."""
from pathlib import Path
import argparse
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--pandoc', default=os.environ.get('PANDOC', 'pandoc'))
parser.add_argument('--refresh-tex', action='store_true', help='Regenerate TeX from Markdown')
parser.add_argument('--output-dir', type=Path, help='Build outside a frozen export')
args = parser.parse_args()
out = (args.output_dir or ROOT / 'build').resolve()
if (ROOT / 'SHA256SUMS.txt').exists():
    if args.refresh_tex or out == ROOT or ROOT in out.parents:
        parser.error('Frozen exports require an external --output-dir and no --refresh-tex')
if out in {(ROOT / 'paper').resolve(), (ROOT / 'output/pdf').resolve()}:
    parser.error('Build output must not overwrite distributed source or PDF files')
out.mkdir(parents=True, exist_ok=True)
paper = ROOT / 'paper'

def run(cmd, cwd, timeout=45):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=timeout)
    if p.returncode:
        print(p.stdout[-14000:] + p.stderr[-4000:])
        raise SystemExit(p.returncode)

if args.refresh_tex:
    run([args.pandoc, 'manuscript.md', '-f', 'markdown+tex_math_single_backslash',
         '-t', 'latex', '--standalone', '--number-sections', '--natbib',
         '--template', 'template.tex', '--bibliography', 'references.bib',
         '-o', 'manuscript.tex'], paper)
shutil.copyfile(paper / 'manuscript.tex', out / 'manuscript.tex')
shutil.copyfile(paper / 'references.bib', out / 'references.bib')
tex = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'manuscript.tex']
run(tex, out)
run(['bibtex', 'manuscript'], out)
run(tex, out)
run(tex, out)
log = (out / 'manuscript.log').read_text(errors='replace')
for bad in ['undefined references', 'Citation', 'Overfull', 'multiply defined']:
    if bad == 'Citation':
        assert not ('Citation' in log and 'undefined' in log), 'undefined citation'
    else:
        assert bad not in log, bad
print('PASS: PDF compiled; no undefined references/citations, overfull boxes, or duplicate labels')
print('Review', out / 'manuscript.pdf', 'before distributing it.')
