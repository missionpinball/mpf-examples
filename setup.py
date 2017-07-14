"""Mission Pinball Framework example machine files."""

from setuptools import setup

setup(

    name='mpf-examples',
    version='0.50.0-dev1',
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

    include_package_data=True,

)
