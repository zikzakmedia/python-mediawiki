"""
MediaWiki-style markup

Copyright (C) 2012 Raimon Esteve <resteve@zikzakmedia.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""

import re
import random
import locale

from base64 import b64encode
from base64 import b64decode
from StringIO import StringIO

import wikimarkup

_image = re.compile(r'img:(.*)\.(.*)', re.UNICODE)
_attach = re.compile(r'attach:(.*)\.(.*)', re.UNICODE)
_edit = re.compile(r'edit:(.*)\|(.*)', re.UNICODE)
_view = re.compile(r'view:(.*)\|(.*)', re.UNICODE)

class WikiParser(wikimarkup.Parser):

    def parse(self, text):
        text = text.replace('&nbsp;', 'n-b-s-p')
        text = text.replace('&amp;', 'n-a-m-p')
        text = text.replace('&','&amp;')
        text = text.replace('n-b-s-p', '&nbsp;')
        text = text.replace('n-a-m-p', '&amp;')
        text = text.replace('<code>', '<pre>')
        text = text.replace('</code>', '</pre>')

        text = wikimarkup.to_unicode(text)
        text = self.strip(text)

        text = super(WikiParser, self).parse(text)
        text = self.addImage(text)
        text = self.attachDoc(text)
        text = self.recordLink(text)
        text = self.viewRecordLink(text)
        return text

    def viewRecordLink(self, text):
        def record(path):
            return ""

        bits = _view.sub(record, text)
        return bits

    def attachDoc(self, text):
        def document(path):
            file = path.group().replace('attach:','')
            if file.startswith('http') or file.startswith('ftp'):
                return "<a href='%s'>Download File</a>" % (file)
            else:
                return ""

        bits = _attach.sub(document, text)
        return bits

    def addImage(self, text):
        def image(path):
            file = path.group().replace('img:','')
            if file.startswith('http') or file.startswith('ftp'):
                return "<img src='%s'/>" % (file)
            else:
                return ""

        bits = _image.sub(image, text)
        return bits

    def recordLink(self, text):
        def record(path):
            return ""

        bits = _edit.sub(record, text)
        return bits

def wiki2html(text, showToc):
    p = WikiParser(show_toc=showToc)
    return p.parse(text)
