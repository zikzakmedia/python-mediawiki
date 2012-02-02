Presentation
============

Convert MediaWiki Syntax to HTML

How to use in a program
=======================

Example for HTML
----------------
In order to use this tool to render wikitext into HTML in a Python program, you can use the following lines:

::

 from wiki import *

 source = ''
 with open("doc/syntax") as f:
    for line in f:
        source += line

 wiki_content = wiki2html(source, True)
 print wiki_content


Doc about Syntax
----------------
See doc dir more about syntax and HTML code generated
