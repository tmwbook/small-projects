__author__ = 'thomas'
import urllib2

from bs4 import BeautifulSoup

import college

base_url = ''

colleges = {}

def get_num_pages(source):
    """find place where the last page link is"""
    pass