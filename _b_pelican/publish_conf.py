#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)

from base_conf import *

OUTPUT_PATH = '../b'
OUTPUT_SOURCES = True
SITEURL = '/b'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
