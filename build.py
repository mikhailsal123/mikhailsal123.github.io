"""Bundle the page and its local images into one HTML file for GitHub Pages."""
from pathlib import Path
from base64 import b64encode
from shutil import copyfile
import mimetypes
import re

root = Path(__file__).parent
html = (root / 'index.html').read_text()
css = (root / 'styles.css').read_text()
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + css + '\n</style>')

def embed_image(match):
    attribute, filename = match.groups()
    path = root / filename
    mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    return attribute + '="data:' + mime + ';base64,' + b64encode(path.read_bytes()).decode() + '"'

html = re.sub(r'(src|data-animation)="(assets/[^\"]+)"', embed_image, html)
(root / 'dist').mkdir(exist_ok=True)
copyfile(root / 'favicon.ico', root / 'dist' / 'favicon.ico')
copyfile(root / 'apple-touch-icon.png', root / 'dist' / 'apple-touch-icon.png')
(root / 'dist' / 'assets').mkdir(exist_ok=True)
copyfile(root / 'assets' / 'globe-icon.png', root / 'dist' / 'assets' / 'globe-icon.png')
(root / 'dist' / 'index.html').write_text(html)
copyfile(root / 'cv.pdf', root / 'dist' / 'cv.pdf')
print('Built dist/index.html and copied dist/cv.pdf')
