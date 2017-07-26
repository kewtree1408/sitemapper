import unittest
from lxml import etree
from utils import (
    get_root_url,
    iter_re_for_href,
    xml_output,
)


class TestUtils(unittest.TestCase):
    def test_get_root_url(self):
        long_url = 'https://github.com/tox-dev/tox/blob/master/CHANGELOG'
        short_url = 'https://github.com'
        expected_url = 'https://github.com/'
        self.assertEqual(get_root_url(long_url), expected_url)
        self.assertEqual(get_root_url(short_url), expected_url)

    def test_iter_re_for_href(self):
        raw_page = """
        <li class="tier-1 element-1">\n
        <a href="/about/" >About</a>\n
        <ul class="subnav menu">
        <li class="tier-2 element-1" role="treeitem">
        <a href="/about/apps/" title="">Applications</a></li>
        <li class="tier-2 element-2" role="treeitem">
        <a href="/about/quotes/" title="">Quotes</a></li>
        <li class="tier-2 element-3" role="treeitem">
        <a href="/about/gettingstarted/" title="">Getting Started</a></li>
        """

        href_results = [
            '/about/',
            '/about/apps/',
            '/about/quotes/',
            '/about/gettingstarted/',
        ]
        self.assertListEqual(
            sorted(list(iter_re_for_href(raw_page))),
            sorted(href_results)
        )

    def test_xml_output_depth_1(self):
        xml_result = xml_output('http://google.com', default=False, depth=1)
        result = etree.tostring(
            xml_result,
            pretty_print=True,
            xml_declaration=True,
            encoding='UTF-8'
        )
        with open('tests/data/google_first_page.txt', 'r') as f:
            self.assertEqual(sorted(f.read()), sorted(result))

    def test_xml_output_depth_3(self):
        xml_result = xml_output('https://python.org', default=False, depth=3)
        result = etree.tostring(
            xml_result,
            pretty_print=True,
            xml_declaration=True,
            encoding='UTF-8'
        )
        with open('tests/data/python_top_three.txt', 'r') as f:
            self.assertEqual(sorted(f.read()), sorted(result))
