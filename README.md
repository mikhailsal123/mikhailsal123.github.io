# Personal website

Live: https://mikhailsal123.github.io/

Repository: https://github.com/mikhailsal123/mikhailsal123.github.io

## Edit

- Text and links: `index.html`.
- CV: replace `cv.pdf` with the updated PDF.
- Layout and typography: `styles.css`.
- Photo: replace `assets/photo.jpg` to update the portrait. The build script includes it automatically.

## Preview and publish

Run `python3 build.py` to create `dist/index.html`. To preview, run `python3 -m http.server 8000` and open http://localhost:8000/dist/.

Publish by uploading `dist/index.html` and `dist/cv.pdf` at the repository root on the `main` branch. GitHub Pages deploys automatically.

The page uses plain HTML and CSS, with no JavaScript or external dependencies.
