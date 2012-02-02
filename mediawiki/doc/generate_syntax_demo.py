from mediawiki import *

source = ''
with open("syntax") as f:
    for line in f:
        source += line

wiki_content = wiki2html(source, True)
print wiki_content
