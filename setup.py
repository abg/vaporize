#!/usr/bin/env python

from distutils.core import setup

try:
    readme = open('README.rst', 'r').read()
except IOError:
    readme = ''

setup(
    name='vaporize',
    description='A clean and consistent library for the Rackspace Cloud / OpenStack',
    long_description=readme,
    author='Michael Lavers',
    author_email='kolanos@gmail.com',
    url='https://github.com/kolanos/vaporize',
    version='0.1.6',
    license='MIT',
    install_requires=['requests', 'python-dateutil'],
    packages=['vaporize'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
    ],
)