from __future__ import print_function
from setuptools import setup
import io
import os

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name='unitoracle',
    license='BSD 3-clause',
    author='Smithsonian Astrophysical Observatory / Chandra X-Ray Center',
    requires=['astropy', 'numpy'],
    install_requires=['astropy', 'numpy'],
    author_email='jbudynkiewicz@cfa.harvard.edu',
    url='https://github.com/jbudynk/unitoracle',
    description='Simple flux unit converter for testing',
    packages=['unitoracle'],
    include_package_data=True,
    platforms='Linux, Mac OSX',
    classifiers = [
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Astronomers, Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)