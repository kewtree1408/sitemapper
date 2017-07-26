#!/usr/bin/env python

import click
from src.utils import (
    get_root_url,
    write_into_file,
    xml_file_output,
)


@click.command()
@click.option('--url', prompt='Input site',
              help='Input the link for sitemapper here.')
@click.option('--proto-format', prompt='Expected format',
              help="""
              There are 2 formats for output: file and xml.
              For the file format there will be created the file called
              <./sitemap.txt>
              """,
              default='file')
def get_sitemap(url, proto_format):
    root_url = get_root_url(url)
    if proto_format == 'file':
        fname = 'sitemap.txt'
        write_into_file(url, fname)
        click.echo("Look at your sitemap in <%s>" % fname)
    else:
        fname = 'sitemap.xml'
        xml_file_output(url, fname, default=True)
        click.echo("Look at your sitemap in <%s>" % fname)


if __name__ == '__main__':
    get_sitemap()
