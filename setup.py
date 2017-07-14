"""Mission Pinball Framework example machine files."""

import os
from os.path import join, dirname
from setuptools import setup

from _version import version

PACKAGE_FILES_EXCLUDED_EXT = ['pyc']

data_files = list()

for root, subFolders, files in os.walk('.'):
    for fn in files:

        ext = fn.split('.')[-1].lower()
        if ext in PACKAGE_FILES_EXCLUDED_EXT:
            continue

        filename = join(root, fn)
        directory = dirname(filename)
        data_files.append((directory, [filename]))

setup(

    name='mpf-examples',
    version=version,
    description='Mission Pinball Framework example machine files',
    long_description="""This repository contains examples for the Mission
Pinball Framework, including complete configuration and test files for each
step in the MPF tutorial.""",
    url='http://missionpinball.org',
    author='The Mission Pinball Framework Team',
    author_email='brian@missionpinball.org',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Artistic Software',
        'Topic :: Games/Entertainment :: Arcade'

    ],

    keywords='pinball',

    zip_safe=False,

    data_files=data_files,

)
