# Copyright (c) 2021 Roger Thomas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rapi

with open("README.md", "r") as f:
    readme = f.read()

setup(name="rapi",
      version=rapi.__version__,
      author=rapi.__author_name__,
      author_email=rapi.__author_email__,
      url=rapi.__package_url__,
      py_modules=["rapi"],
      description="Raspberry Pi checking library",
      long_description=readme,
      license="MIT",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Programming Language :: Python :: 3",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Topic :: Software Development :: Libraries",
          "Topic :: Utilities",
      ],
      python_requires=">=3.5",
      )
