# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

# Vagrant / tox workaround (http://bugs.python.org/issue8876#msg208792)
if os.environ.get('USER','') == 'vagrant':
    del os.link

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.rst')) as f:
    README = f.read()

setup(
    name='django-badgify',
    version='0.1.0',
    description='Badges app for Django',
    long_description=README,
    author='Gilles Fabio',
    author_email='gilles.fabio@gmail.com',
    url='http://github.com/ulule/django-badgify',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
