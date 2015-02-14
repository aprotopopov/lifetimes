#!/usr/bin/env python
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='Lifetimes',
      version='0.1.0',
      description='Measure customer lifetime value in Python',
      author='Cam Davidson-Pilon',
      author_email='cam.davidson.pilon@gmaillcom',
      packages=['lifetimes'],
      license="MIT",
      keywords="customer lifetime value, clv, ltv",
      url="https://github.com/CamDavidsonPilon/lifetimes",
      long_description=read('README.txt'),
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        ],
      install_requires=[
        "numpy",
        "scipy",
        "pandas>=0.14",
        ],
     )
