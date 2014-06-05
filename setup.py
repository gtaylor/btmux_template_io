#!/usr/bin/env python

import btmux_template_io

from setuptools import setup

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Programming Language :: Python :: 2.7',
]

KEYWORDS = 'btmux battletech mud mux template'

setup(
    name='btmux_template_io',
    version=btmux_template_io.__version__,
    description='BattletechMUX template parsing/representation',
    long_description=LONG_DESCRIPTION,
    author='Gregory Taylor',
    author_email='gtaylor@gc-taylor.com',
    url='https://github.com/gtaylor/btmux_template_io',
    download_url='http://pypi.python.org/pypi/btmux_template_io/',
    packages=['btmux_template_io'],
    platforms=['Platform Independent'],
    license='BSD',
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    requires=[]
)
