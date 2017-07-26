import requests
import re
import utils
import datetime
from lxml import etree


class MetaData(object):
    def __init__(self, location, lastmod=None, changefreq=None, priority=0.5):
        self.location = location
        self.lastmod = lastmod
        self.changefreq = changefreq
        self.priority = priority

    def xml(self):
        """
        :return: etree.Element with meta data
        """
        url = etree.Element('url')
        loc = etree.SubElement(url, 'loc')
        loc.text = self.location
        lastmod = etree.SubElement(url, 'lastmod')
        lastmod.text = self.lastmod
        changefreq = etree.SubElement(url, 'changefreq')
        changefreq.text = self.changefreq
        priority = etree.SubElement(url, 'priority')
        priority.text = str(self.priority)
        return url


class Crawler(object):
    """
    Crawler for links on the site.
    Following the rules on https://www.sitemaps.org/protocol.html
    """

    def __init__(self, root_url):
        self.root = root_url if root_url.endswith('/') else root_url+'/'
        self.any_proto = root_url.split('://', 1)[-1]
        self.max_depth = 10

    def get_all_urls(self, url, flatten_map=None):
        if not flatten_map:
            flatten_map = set()

        if len(flatten_map) > self.max_depth:
            return flatten_map

        for href in self.get_hrefs_per_page(url):
            if href not in flatten_map:
                flatten_map.add(href)
                self.get_all_urls(href, flatten_map)

        return flatten_map

    def get_flatten_urls(self):
        """
        All urls are stored there.
        """
        return list(self.get_all_urls(self.root))

    def get_all_info(self, default=False):
        default_params = {
            'lastmod': utils.get_text_date(datetime.datetime.today()),
            'changefreq': 'always',
        }

        for href in self.get_flatten_urls():
            if default:
                yield MetaData(
                    location=href,
                    lastmod=default_params['lastmod'],
                    changefreq=default_params['changefreq'],
                )
            else:
                yield MetaData(location=href)

    def get_hrefs_per_page(self, url):
        data = requests.get(url)
        if data.status_code != 200:
            yield None

        utf_data = data.content

        for href in utils.iter_re_for_href(utf_data):
            href = href.decode('utf-8')
            if href.startswith(self.root):
                yield href
            elif href.startswith('//'):
                # pass double slashes
                clear_href = href[2:]
                if clear_href.startswith(self.any_proto):
                    yield clear_href
            elif href.startswith('/'):
                # should join the root url with the rest part
                yield self.root + href[1:]
