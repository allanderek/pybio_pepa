from setuptools import setup

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import pybio_pepa

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

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
    name='pybio_pepa',
    version=pybio_pepa.__version__,
    url='http://github.com/allanderek/pybio_pepa/',
    license='MIT',
    author='Allan Clark',
    tests_require=['pytest'],
    install_requires = [ 'pyparsing' ],
    cmdclass={'test': PyTest},
    author_email='allan.clark@gmail.com',
    description='Library to manipulate Bio-PEPA files',
    long_description=long_description,
    packages=['pybio_pepa'],
    include_package_data=True,
    platforms='any',
    # test_suite='pybio_pepa.test.test_pybio_pepa',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
