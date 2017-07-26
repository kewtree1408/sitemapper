#!/usr/bin/env python

import click
from src.utils import get_root_url, get_file_sitemap


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
        get_file_sitemap(url)
        click.echo("Look at your sitemap in <sitemap.txt>")
    else:
        click.echo("Not implemented yet")


if __name__ == '__main__':
    get_sitemap()
