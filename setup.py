# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

import pigule


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='pigule',
    version=pigule.__version__,
    url='http://github.com/marienfressinaud/pigule',
    license='MIT License',
    description='A cell-based game.',
    long_description=open('README.md').read(),
    author='Marien Fressinaud',
    author_email='dev@marienfressinaud.fr',
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={
        'test': PyTest
    },
    packages=['pigule'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only'
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
