#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-little-printer-menu',
    version='0.1',
    description='A simple Django app to create a weekly menu formatted for the BERG Cloud Little Printer.',
    author='David Moss',
    author_email='david@illansis.com',
    license='Python License',
    url='https://github.com/davidjamesmoss/django-little-printer-menu',
    packages=find_packages(),
    install_requires=['requests','django-crispy-forms'],
    package_data={
        '': [
            'templates/menu/*.html',
            'static/menu/images/*.png',
        ],
    },
)
