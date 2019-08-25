#!/usr/bin/env python3
"""
Pixel Art Fx

:copyright: 2015 Aurélien Gâteau.
:license: Apache 2.0.
"""
from setuptools import setup

DESCRIPTION = 'Pixel Art effects'


setup(name='pafx',
      version='0.1.0',
      description=DESCRIPTION,
      author='Aurélien Gâteau',
      author_email='mail@agateau.com',
      license='Apacke 2.0',
      platforms=['any'],
      url='https://github.com/agateau/pafx',
      install_requires=[
          'pillow',
      ],
      packages=['pafx'],
      )
