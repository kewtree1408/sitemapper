#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import (
    setup,
    find_packages,
)
import re
import os

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


packages = find_packages('src')
packages_data = get_package_data('src')


setup(
    name='sitemapper',
    version='0.1',
    url='https://github.com/kewtree1408/sitemapper/',
    license='BSD',
    description='The command line interface for getting a sitemap for any site',
    author='Victoria Karpova',
    author_email='me@vika.space',
    package_dir={'': 'src'},
    packages=packages,
    package_data=packages_data,
)
