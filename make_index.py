""" Build index from directory listing

make_index.py [--dir </path/to/directory>]
"""

INDEX_TEMPLATE = r"""<!DOCTYPE html>
<html>

<head>
    <title>${header}</title>
    <style>
        body {
          background-color: #fcfcfc;
          color: #223f4a;
          font-size: 16px;
        }
        @media screen and (orientation:landscape) {
        body {
          margin: 1em 10% 2em 10%;
        }
        }
        @media screen and (orientation:landscape) {
          margin: 1em;
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
Joshua Chen 2017
</footer>

</body>

</html>
"""

EXCLUDED = [
'.git',
'site',
'index.html',
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
