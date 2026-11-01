"""Give both research GIFs matching canvases without stretching their contents."""
from pathlib import Path
from shutil import copyfile
from PIL import Image, ImageOps

ROOT = Path(__file__).parent
ASSETS = ROOT / 'assets'
SIZE = (1000, 636)
BACKGROUND = (253, 253, 253)


def prepare(source_name, output_name, poster_frame):
    source = Image.open(ASSETS / source_name)
    frames, durations = [], []
    loop = source.info.get('loop', 0)
    for index in range(source.n_frames):
        source.seek(index)
        content = ImageOps.contain(source.convert('RGB'), SIZE, Image.Resampling.LANCZOS)
        canvas = Image.new('RGB', SIZE, BACKGROUND)
        canvas.paste(content, ((SIZE[0] - content.width) // 2, (SIZE[1] - content.height) // 2))
        frames.append(canvas)
        durations.append(source.info.get('duration', 200))
    frames[0].save(
        ASSETS / output_name, save_all=True, append_images=frames[1:],
        duration=durations, loop=loop, disposal=2,
    )
    frames[poster_frame].save(ASSETS / output_name.replace('.gif', '-still.png'), optimize=True)


if __name__ == '__main__':
    prepare('neurocotans.gif', 'neurocotans-layout.gif', 18)
    prepare('latentrxnflow.gif', 'latentrxnflow-layout.gif', 0)
