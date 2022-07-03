# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 13:22
# @Author  : llc
# @File    : setup.py
import os
import re

from setuptools import setup

long_description = open('README.md', 'r', encoding='utf-8').read()

version_file = os.path.join(os.path.dirname(__file__), 'PyQRibbon', '__version__.py')
with open(version_file, 'r', encoding='utf-8') as f:
    version = re.findall(r"__version__ = '(.*?)'", f.read())[0]

setup(
    name="PyQRibbon",
    version=version,
    url='https://github.com/luolingchun/PyQRibbon',
    description='PyQRibbon',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='llc',
    author_email='luolingchun@outlook.com',
    license='GPLv3',
    packages=['PyQRibbon', 'PyQRibbon.i18n', 'PyQRibbon.theme', 'PyQRibbon.widgets'],
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=False,
    platforms='any',
    install_requires=['PyQt5']
)
