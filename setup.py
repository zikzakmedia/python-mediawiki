#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    MediaWiki Syntax to HTML

    :copyright: (c) 2012 by Raimon Esteve.
    :license: GPLv3, see LICENSE for more details

    A simple to use python library to access convert wiki syntax
    to HTML
'''

from setuptools import setup
import mediawiki

setup(
    name = 'mediawiki',
    version=mediawiki.__version__,
    url='http://github.com/zikzakmedia/python-mediawiki',
    license='GPLv3+',
    author='Raimon Esteve',
    author_email='zikzak@zikzakmedia.com',
    description='MediaWiki Syntax to HTML',
    packages=[
        'mediawiki',
        'mediawiki.wikimarkup',
        'mediawiki.doc',
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

