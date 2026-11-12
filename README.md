# atriumintelligence.net

This repo builds the Atrium Intelligence website with Python. The copy lives in `content.py`, the page layouts are Jinja2 templates in `templates/`, and `build.py` generates the finished HTML. GitHub Actions rebuilds the site and publishes it to GitHub Pages for free on every push to `main`.

The **Live demo** page embeds the Smart Brew Streamlit app (https://smartbrewpitchdemo.streamlit.app/) and also links out to it.

## Edit the site

- **Words:** edit `content.py`. Headlines, services, questions, the demo guide and contact details are all in that file.
- **Layout:** edit the files in `templates/`.
- **Look:** edit `static/style.css`. The colors and type scale are set at the top of the file.
- **Hero drawing:** `atrium_plan_svg()` in `build.py` draws it. Room names come from `PLAN_ROOMS` in `content.py`.

Preview locally:

```bash
pip install -r requirements.txt
python build.py --serve      # then open http://localhost:8000
```

## Go live (one-time setup)

1. Push this repo to GitHub as **AtriumIntelligence/atrium-website**. The repo must be public to use GitHub Pages on the free plan.
2. On GitHub, open **Settings → Pages** and set **Source** to **GitHub Actions**. The included workflow then builds and deploys the site on every push.
3. In the same **Settings → Pages** screen, set **Custom domain** to `www.atriumintelligence.net`. Once it's verified, tick **Enforce HTTPS**.
4. Change the DNS records at the company where atriumintelligence.net is registered:

   | Type  | Host / Name | Value |
   |-------|-------------|-------|
   | CNAME | `www` | `atriumintelligence.github.io` |
   | A     | `@` | `185.199.108.153` |
   | A     | `@` | `185.199.109.153` |
   | A     | `@` | `185.199.110.153` |
   | A     | `@` | `185.199.111.153` |

   Remove any older A or CNAME records that point at the old website builder. DNS changes can take a few hours to take effect.
5. Cancel the old website builder plan once the new site loads at your domain.

## Notes

- Pricing is intentionally left off the site for now.
- The demo is free-tier Streamlit, so it sleeps after a period with no visitors. The demo page tells visitors how to wake it, and you should open it yourself before a pitch.
