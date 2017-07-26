#! /usr/bin/env python

import re
import codecs
from lxml import etree
from crawler import Crawler


def write_into_file(url, fname):
    """
    Create and save the sitemap data in the <fname> file.
    """
    with codecs.open(fname, "w", "utf-8") as f:
        for link in Crawler(url).get_hrefs():
            f.write(link)
            f.write('\n')


def xml_output(url, default=False):
    """
    XML output for sitemap.
    Following this protocol: https://www.sitemaps.org/protocol.html
    Example:
    <?xml version="1.0" encoding="UTF-8"?>

    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>http://www.example.com/</loc>
      <lastmod>2005-01-01</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
   </url>
    """
    root = etree.Element('urlset')
    for url_data in Crawler(url).get_all_info(default):
        # url_data is a crawler.MetaData object
        root.append(url_data.xml())
    return root


def xml_file_output(url, fname, default=False):
    urls_tree = xml_output(url, default)
    with codecs.open(fname, "w", "utf-8") as f:
        f.write(etree.tostring(urls_tree, pretty_print=True))


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


def get_text_date(date):
    """
    :param date_and_time: datetime Object
    """
    return '{year}-{month}-{day}'.format(
                year=date.year,
                month=date.month,
                day=date.day
            )
