#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.getcwd())

ROOT = os.path.realpath(os.getcwd())
#THEME = os.path.join(ROOT,'theme')

THEME = 'theme'
AUTHOR = u"Manasvi Gupta"
SITETITLE= u"Manasvi Gupta's blog"
SITENAME = u"Will code for FUN!"
SITESUBTITLE = u"Open Source, Startups, Machine Learning, Functional Programming"
SITEURL = ''


RELATIVE_URLS = False
#PAGE_DIR='src/pages'
TIMEZONE = 'Europe/London'
GITHUB_REPO = "https://github.com/manasvigupta/website"
GIT_BRANCH = 'master'
GITHUB_EDIT_PREFIX = "%s/blob/%s" % (GITHUB_REPO, GIT_BRANCH)
TWITTER_USERNAME = 'manasvigupta'
TWITTER_SHARE_RELATED = TWITTER_USERNAME
TWITTER_SHARE_VIA = TWITTER_USERNAME


DEFAULT_LANG='en'
GOOGLE_ANALYTICS = "UA-34383847-1"
# Social widgets
# Name , link, new page
SOCIAL = (

     ('Me', '/profile.html' , False ),
     ('Twitter', 'https://twitter.com/manasvigupta', True),
    ('Linkedin', 'http://www.linkedin.com/manasvigupta', True),
    ('Github', 'http://github.com/manasvigupta/', True),
         )

# Links
LINKS = (

         )

DEFAULT_PAGINATION = 7
DEFAULT_ORPHANS = 1

DISQUS_SITENAME = "rach-belaid-blog"

DEFAULT_DATE_FORMAT = "%d %b %Y"
# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),('extra/CNAME', 'CNAME'),)

#DIRECT_TEMPLATES= ['index', 'tags', 'categories', 'archives','profile'] #,'resume','projects']
#EXTRA_TEMPLATES_PATHS=['extra',]
PROFILE_SAVE_AS = 'profile.html'
RESUME_SAVE_AS = 'resume.html'
PROJECTS_SAVE_AS = 'projects.html'
#PLUGIN_PATH = "plugins"
#from plugins.bitly import bitly_plugin
#PLUGINS = ['pelican-bitly',]

try:
    from local_settings import *
except ImportError:
    pass
    
    
    
