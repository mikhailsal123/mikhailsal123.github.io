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
    path = root / match.group(1)
    mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    return 'src="data:' + mime + ';base64,' + b64encode(path.read_bytes()).decode() + '"'

html = re.sub(r'src="(assets/[^\"]+)"', embed_image, html)
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'index.html').write_text(html)
copyfile(root / 'cv.pdf', root / 'dist' / 'cv.pdf')
print('Built dist/index.html and copied dist/cv.pdf')
