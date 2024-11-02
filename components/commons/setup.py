import os
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.dirname(os.path.abspath(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md"), "r") as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="deepsea-commons",
    version="0.0.1",
    description="Deepsea Shared Library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/stonezhong/deepsea/blob/master/README.md",
    author="Stone Zhong",
    author_email="stone.zhong@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_dir = {'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=["pydantic>=2.6.3"]
)
