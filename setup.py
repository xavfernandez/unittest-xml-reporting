#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'unittest-xml-reporting',
    version = '1.0',
    author = 'Daniel Fernandes Martins',
    author_email = 'daniel.tritone@gmail.com',
    description = 'PyUnit-based test runner with JUnit like XML reporting.',
    license = 'LGPL',
    platforms = ['Any'],
    keywords = ['pyunit', 'unittest', 'junit xml', 'report', 'testrunner'],
    url = 'http://github.com/danielfm/unittest-xml-reporting/tree/master/',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    py_modules = ['xmlrunner'],
    test_suite = 'tests.testsuite',
)
