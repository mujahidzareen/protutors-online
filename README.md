# ProTutors Online

Animated, responsive, 36-page international online tutoring website for primary
through Grade 12 / FSc students. Includes subjects, curricula, exam preparation,
UK/US/Gulf pages, illustrative regional prices, lesson calculators, FAQs, and a
local demo-enquiry wizard. This is a service website, not an LMS.

## Publish to GitHub Pages

1. Push this repository to your GitHub account with `main` as the default branch.
2. Repository Settings → Pages → Build and deployment → Source: GitHub Actions.
3. Run the Publish ProTutors Online workflow from the Actions tab, or push to main.
4. Use the website URL returned by the successful deployment.

The workflow adapts links and assets for both project sites and account-root sites.
It uses GitHub's built-in workflow token, so no password or personal token belongs
in this repository. No credentials or private account data are included.

## Edit

Page content and layouts: `scripts/build.py`.
Original homepage and base design: `src/`.
Multipage styles and animations: `dist/pages.css` and `dist/app.js`.
Run `python3 scripts/build.py` to rebuild the HTML. The GitHub Pages workflow then
sets the correct repository base path and sitemap automatically.

To preview locally, run `python3 -m http.server 8000 --directory dist` and open
http://localhost:8000/. The static files assume a web server rather than file://.

## Before accepting enquiries

Prices are labelled sample amounts. The form prepares an enquiry for copying or
downloading; no request is sent, no payment is taken, and no session is reserved.
Add your approved business details and enquiry service before launch.

An editable WordPress + Elementor version is supplied separately. WordPress PHP
cannot be hosted on GitHub Pages; this repository publishes the static website.
