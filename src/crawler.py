import requests
import re
import utils

class MetaData(object):
    def __init__(self, location, lastmod=None, changefreq=None, priority=None):
        self.location = location
        self.lastmod = lastmod
        self.changefreq = changefreq
        self.priority = priority


class Crawler(object):
    """
    Crawler for links on the site.
    Following the rules on https://www.sitemaps.org/protocol.html
    """

    def __init__(self, root_url):
        self.root = root_url if root_url.endswith('/') else root_url+'/'
        self.any_proto = root_url.split('://', 1)[-1]

    def _iter_re_for_href(self, data):
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

    def urls(self):
        """
        All hierarhy is stored there.
        """
        for href in self.get_hrefs():
            print href

    def get_hrefs(self):
        data = requests.get(self.root)
        if data.status_code != 200:
            yield None

        utf_data = data.content

        for href in self._iter_re_for_href(utf_data):
            href = href.decode('utf-8')
            # yield href
            if href.startswith(self.root):
                yield href
            elif href.startswith('//'):
                # pass double slashes
                clear_href = href[2:]
                # print clear_href
                if clear_href.startswith(self.any_proto):
                    yield clear_href
            elif href.startswith('/'):
                # should join the root url with the rest part
                yield self.root + href[1:]
