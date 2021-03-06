# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='aimay',
    version='1.1.0',
    description='LINE Bot AI May',
    long_description=readme,
    author='suna',
    author_email='suna@xmpp.is',
    url='https://github.com/ghsable/aimay',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', '.github', '.maintenance', '.readme'))
)
