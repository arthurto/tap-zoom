#!/usr/bin/env python

from setuptools import setup

setup(name='tap-zoom',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Zoom API',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_zoom'],
      install_requires=[
      ],
      entry_points='''
          [console_scripts]
          tap-zoom=tap_zoom:main
      ''',
      packages=['tap_zoom'],
      package_data = {
          'tap_zoom': ['schemas/*.json'],
      }
)