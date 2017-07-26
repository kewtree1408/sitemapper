#! /usr/bin/env python

import re
import codecs
from crawler import Crawler


def get_file_sitemap(url):
    fname = 'sitemap.txt'
    with codecs.open(fname, "w", "utf-8") as f:
        for link in Crawler(url).get_hrefs():
            f.write(link)
            f.write('\n')


def xml_output(crawler):
    """
    XML output for sitemap
    """
    pass


def file_output(crawler):
    """
    File output for sitemap
    """
    pass


def clear_href(raw_href):
    """
    :param raw_href: https://ru.wikipedia.org/wiki/ " title="\xd0\x9a" ... >
    :return: https://ru.wikipedia.org/wiki/
    """
    pass

def get_root_url(long_url):
    root_urls = re.findall(r'\w+://.*?/', long_url, flags=re.IGNORECASE)
    root_url = root_urls[0] if root_urls else long_url
    return root_url
