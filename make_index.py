""" Build index from directory listing

make_index.py [--dir </path/to/directory>]
"""

INDEX_TEMPLATE = r"""<!DOCTYPE html>
<html>

<head>
    <title>${header}</title>
    <link href="https://fonts.googleapis.com/css?family=Fira+Mono:400,500" rel="stylesheet">
    <style>
        body {
          margin: 4em 4em 4em 4em;
          background-color: #f6f6f6;
          color: #1f3a44;
          font-size: 16px;
          font-family: 'Fira Mono', monospace;
        }
        footer {
          position: absolute;
          bottom: 1em;
          box-shadow: 0px 1px 3px 1px #a0a0a0;
          background-color: #ffffff;
          padding: 1px;
          text-align: center;
          font-size: 0.7em;
        }
        footer a {
          color: #1f3a44;
        }
    </style>
</head>

<body>

<h2>${breadcrumb}</h2>
<h1>${header}</h1>

<ul>
% for dname in dnames:
    <li class="dirbullet"><a href="${dname}">${dname}/<a></li>
% endfor
% for fname in fnames:
    <li class="filebullet"><a href="${fname}">${fname}<a></li>
% endfor
</ul>

<footer>
<script src="https://use.fontawesome.com/fa49007a92.js"></script>
Joshua Chen 2017
<a href="${depth}about.html">
    <span class="fa fa-hand-spock-o" id="hi"
    onmouseover="javascript:document.getElementById('hi').setAttribute('class','fa fa-hand-lizard-o')"
    onmouseout="javascript:document.getElementById('hi').setAttribute('class','fa fa-hand-spock-o')"></span>
</a>
</footer>

</body>

</html>
"""

EXCLUDED = [
'.git',
'site',
'index.html',
'about.html',
'make_index.py']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template

def process(directory, header, breadcrumb, depth):
    print('Processing' + directory + '...')

    header = header if header else os.path.basename(directory)
    fnames = [name for name in sorted(os.listdir(directory))
              if os.path.isfile(directory + '/' + name) and name not in EXCLUDED]
    dnames = [name for name in sorted(os.listdir(directory))
              if os.path.isdir(directory + '/' + name) and name not in EXCLUDED]

    out = open(directory + '/index.html', 'w')
    out.write(Template(INDEX_TEMPLATE).render(dnames=dnames, fnames=fnames, header=header, breadcrumb=breadcrumb, depth=depth))
    out.close()

    for dname in dnames:
        process(directory + '/' + dname, '', breadcrumb + header + ' &gt;', depth + '../')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir")
    args = parser.parse_args()
    directory = args.dir if args.dir else os.getcwd()

    process(directory, '', '', '')

if __name__ == '__main__':
    main()
