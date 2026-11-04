"""Adapt root-relative site assets and links to the GitHub Pages project path."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse,re
p=argparse.ArgumentParser();p.add_argument('--base-path',default='');p.add_argument('--site-url',required=True);p.add_argument('--directory',default='dist');a=p.parse_args()
root=Path(a.directory);base='/' + a.base_path.strip('/') if a.base_path.strip('/') else ''
if not re.fullmatch(r'(?:/[A-Za-z0-9_.-]+)*',base):raise SystemExit('Unexpected Pages base path')
origin=urlsplit(a.site_url)
if origin.scheme!='https' or not origin.netloc:raise SystemExit('An HTTPS site URL is required')
for f in root.rglob('*.html'):
    text=f.read_text()
    text=re.sub(r'(?P<prefix>\b(?:href|src|action)=")(?!//)/',lambda m:m['prefix']+base+'/',text)
    f.write_text(text)
(root/'.nojekyll').touch()
urls=[]
for f in sorted(root.rglob('index.html')):
    path=f.parent.relative_to(root).as_posix();path='' if path=='.'else path
    urls.append(a.site_url.rstrip('/')+'/'+(path+'/'if path else ''))
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>'for u in urls)+'</urlset>')
print(f'Prepared {len(urls)} pages for {base or "/"}')
