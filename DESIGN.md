# Design references

Reviewed the rendered personal pages on 2026-10-31:

- https://jonbarron.info/ — compact biography beside a portrait, ordinary text links, research presented as a readable document.
- https://shurans.github.io/ — clear name and biography, restrained typography, portrait integrated with personal information.
- https://www.cs.cmu.edu/~dpathak/ — direct links, useful research detail, simple text hierarchy.

Applied to this page: a 720px reading width; a modest name heading; a short first-person introduction with the portrait alongside it; one GitHub profile link; two text entries with linked titles and factual descriptions. A nearly white, warm background keeps the page quiet. No top navigation, logo, slogans, arrows, project numbers, tags, calls to action, repeated links, photo caption, shadows, decorative frame, or footer.

The portrait uses the owner's photo. No affiliations, awards, publication venues, or research results have been invented. Project descriptions come from the project READMEs and the local NeuroCOTANS README reviewed during the original build.

## Responsive verification

Phones up to 560px use a separate portrait-first, single-column composition: a centered 136px portrait and name, full-width biography, centered contact links, 20px side gutters, and paper statuses on separate lines. Tablet widths through 832px use a 220px portrait and 24px side gutters. Desktop keeps the wide page and 300px portrait. Desktop margin adjustments do not affect phone gutters.

Verified in an isolated headless Chromium at 320px, 390px, 430px, 768px, 844px, and 1200px with no horizontal overflow. Visually reviewed full-page screenshots at 320px, 390px, and 1200px. User browser sessions were untouched.
