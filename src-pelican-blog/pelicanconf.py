#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

try:
    import os
    import sys
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)) + '\\')
    import personal_configs as configs
except Exception, ex:
    print '[e] exception: {}'.format(str(ex))
    pass

AUTHOR = u'Viktor Dmitriyev'
SITENAME = u'Yet Another Blog (YAB)'
#SITEURL = 'http://localhost:8000'
SITEURL = 'http://vdmitriyev.github.io/blog'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
LOCALE = "en_US.utf8"
DEFAULT_DATE_FORMAT = ('%B %Y')

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = 'All'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# CONFIGURINT MAIN TOP MENU
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Main', SITEURL),
    ('Interesting', SITEURL + '/category/interesting.html'),
    ('Research', SITEURL + '/category/research.html'),
    ('Thoughts', SITEURL + '/category/thoughts.html'),
    ('Разное', SITEURL + '/category/raznoe.html')
)

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social Widgets in Blogroll section
try:
    LINKS = configs.LINKS
except Exception, ex:
    pass

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = '../blog/'
#STATIC_PATHS = ['images']

try:
    GOOGLE_ANALYTICS = configs.GOOGLE_ANALYTICS
except Exception, ex:
    pass

