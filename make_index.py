""" Build index from directory listing

make_index.py [--dir </path/to/directory>]
"""

INDEX_TEMPLATE = r"""<!DOCTYPE html>
<html>

<head>
    <title>${header}</title>
    <style>
        body {
          margin: 2em 8em 8em 4em;
          background-color: #fcfcfc;
          color: #1f3a44;
          font-size: 16px;
        }
        footer {
          position: absolute;
          bottom: 1em;
          border: 1px solid #1f3a44;
          padding: 1px;
          text-align: center;
          font-size: 0.8em;
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
    <li><a href="${dname}">${dname}/<a></li>
% endfor
% for fname in fnames:
    <li><a href="${fname}">${fname}<a></li>
% endfor
</ul>

<footer>
<script src="https://use.fontawesome.com/fa49007a92.js"></script>
Joshua Chen 2017
<a href="about.html">
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

def process(directory, breadcrumb):
    print('Processing' + directory + '...')

    header = os.path.basename(directory)
    fnames = [name for name in sorted(os.listdir(directory))
              if os.path.isfile(directory + '/' + name) and name not in EXCLUDED]
    dnames = [name for name in sorted(os.listdir(directory))
              if os.path.isdir(directory + '/' + name) and name not in EXCLUDED]

    out = open(directory + '/index.html', 'w')
    out.write(Template(INDEX_TEMPLATE).render(dnames=dnames, fnames=fnames, header=header, breadcrumb=breadcrumb))
    out.close()

    for dname in dnames:
        process(directory + '/' + dname, breadcrumb + header + ' &gt;')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir")
    args = parser.parse_args()
    directory = args.dir if args.dir else os.getcwd()

    process(directory, '')

if __name__ == '__main__':
    main()
