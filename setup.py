# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 13:22
# @Author  : llc
# @File    : setup.py

from setuptools import setup

__version__ = 'v0.9.3'

long_description = """
PyQRibbon是一个实现了ribbon菜单的控件
"""

setup(
    name="PyQRibbon",
    version=__version__,
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
