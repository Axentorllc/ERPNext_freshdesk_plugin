# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in freshdesk_plugin/__init__.py
from freshdesk_plugin import __version__ as version

setup(
	name='freshdesk_plugin',
	version=version,
	description='Plugin fr FreshDesk',
	author='Axentor',
	author_email='opensource@axentor.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
