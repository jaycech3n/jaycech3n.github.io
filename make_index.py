""" Build index from directory listing

make_index.py [--dir </path/to/directory>]
"""

INDEX_TEMPLATE = r"""<!DOCTYPE html>
<html>

<head>
    <title>${header}</title>
    <link href="https://fonts.googleapis.com/css?family=Fira+Mono:400,500" rel="stylesheet">
    <link href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAAn1BMVEUAAAAiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiLhUdjZAAAANHRSTlMAAQIDBAcICQsNEBIaHCgtNTY/TlRVV1ldcXN/goiLjo+XoKaorbfDxcfIzM/c6Ont9/n9yFQzqQAAAK1JREFUKFNtydtagmAYBeFBSMhCDUUrKdxEobmhn3X/19aBjwr4zeG8cC6KAXh8plP2B0BedeFT8LHvr5wBvjQ2gXTp2wBYsPsJbZCmNuy3kQ3gBQZ81bw4Zevaa/9Yi7CWdFTahtI9DCUp+3X95k/0ypMkTYbKGz+oTj2Y1dr0+FZ8g3c1K69/oHbJBYoOVMH5j9TtDQDvcAcaAMzvvwogdAZoBLn1dfDY2BD8A187Mm9IXZdQAAAAAElFTkSuQmCC" rel="icon" type="image/x-icon" />
    <style>
        body {
          margin: 4em 4em 4em 4em;
          background-color: #f6f6f6;
          color: #1f3a44;
          font-size: 16px;
          font-family: 'Fira Mono', monospace;
        }
        footer {
          position: fixed;
          bottom: 1.4em;
          box-shadow: 0px 1px 3px 1px #a0a0a0;
          background-color: #ffffff;
          padding: 1px;
          text-align: center;
          font-size: 0.7em;
        }
        footer a, footer a:visited {
          color: #1f3a44;
        }
        h2 {
          margin-bottom: 1ex;
          font-size: 0.9em;
        }
        h2 a, h2 a:visited {
          color: #1f3a44;
          text-decoration: none;
        }
        h2 a:hover {
          text-decoration: underline;
        }
        h1 {
          margin-top: 0;
          margin-bottom: 1em;
          font-size: 2.2em;
        }
        a {
          color: #0033cc;
        }
        a:visited {
          color: #8C489F;
        }
        ul {
          list-style: none;
          line-height: 1.4em;
        }
        li.dirbullet:before {
          content: "";
          border-color: transparent #1f3a44;
          border-style: solid;
          border-width: 0.35em 0 0.35em 0.45em;
          display: block;
          height: 0;
          width: 0;
          left: -1em;
          top: 0.9em;
          position: relative;
        }
    </style>
</head>

<body>

<h2>
% if not breadcrumb:
    Index of
% else:
    % for i, dir in enumerate(breadcrumb):
        <a href="${'../'*(depth-i)}">${dir}</a>
        &nbsp;&gt;&nbsp;
    % endfor
%endif
</h2>
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
<a href="${'../'*depth}about.html">
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
    print(breadcrumb)

    header = header if header else os.path.basename(directory)
    contents = sorted(os.listdir(directory))
    fnames = [name for name in contents
              if os.path.isfile(directory + '/' + name) and name not in EXCLUDED]
    dnames = [name for name in contents
              if os.path.isdir(directory + '/' + name) and name not in EXCLUDED]

    out = open(directory + '/index.html', 'w')
    out.write(Template(INDEX_TEMPLATE).render(dnames=dnames, fnames=fnames, header=header, breadcrumb=breadcrumb, depth=depth))
    out.close()

    breadcrumb.append(header)

    for dname in dnames:
        process(directory + '/' + dname, '', breadcrumb, depth + 1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir")
    args = parser.parse_args()
    directory = args.dir if args.dir else os.getcwd()

    process(directory, '', [], 0)

if __name__ == '__main__':
    main()
