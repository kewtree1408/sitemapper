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
        for link in Crawler(url).get_flatten_urls():
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
    root = etree.Element('urlset',
                         xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url_data in Crawler(url).get_all_info(default):
        # url_data is a crawler.MetaData object
        root.append(url_data.xml())
    return root


def xml_file_output(url, fname, default=False):
    urls_tree = xml_output(url, default)
    with codecs.open(fname, "w", "utf-8") as f:
        f.write(
                etree.tostring(
                    urls_tree,
                    pretty_print=True,
                    xml_declaration=True,
                    encoding='UTF-8'
                )
            )


def get_root_url(long_url):
    root_urls = re.findall(r'\w+://.*?/', long_url, flags=re.IGNORECASE)
    root_url = root_urls[0] if root_urls else long_url
    return root_url


def iter_re_for_href(data):
    """
    :param data: raw data from the url with differents hrefs, such as:
    <a href="(pattern=https://docs.python.org/3/library/asyncio.html)">
    or
    <a href='(pattern=https://docs.python.org/3/library/asyncio.html)'>
    :return: generator
    """
    for item in re.finditer(
        r'<a href=["|\'](?P<href>.*?)["|\']',
        data,
        flags=re.IGNORECASE
    ):
        yield item.group('href')


def get_text_date(date):
    """
    :param date_and_time: datetime Object
    """
    return '{year}-{month}-{day}'.format(
                year=date.year,
                month=date.month,
                day=date.day
            )
