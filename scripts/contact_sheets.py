"""Optional visual-QA sheets from existing Poppler page renders; needs Pillow."""
from pathlib import Path
import argparse
from PIL import Image, ImageOps, ImageDraw
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--pages-dir', type=Path, default=root/'tmp/pdfs')
args=parser.parse_args()
pages=sorted(args.pages_dir.glob('page-*.png'))
assert pages
for offset in range(0,len(pages),6):
    group=pages[offset:offset+6]
    images=[Image.open(p).convert('RGB') for p in group]
    w=max(im.width for im in images); h=max(im.height for im in images)+24
    sheet=Image.new('RGB',(2*w,3*h),'#c8c8c8')
    draw=ImageDraw.Draw(sheet)
    for i,im in enumerate(images):
        x=(i%2)*w; y=(i//2)*h
        draw.text((x+8,y+5),f'Page {offset+i+1}',fill='black')
        sheet.paste(im,(x,y+24))
    sheet.save(args.pages_dir/f'sheet-{offset//6+1}.png')
print('Contact sheets:',(len(pages)+5)//6)
