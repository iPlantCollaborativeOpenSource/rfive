import os
import setuptools
from rfive.version import get_version

readme = open('README.md').read()

long_description = """
rfive %s
A unified interface into multiple cloud providers.

To install use pip install git+git://git@github.com:iPlantCollaborativeOpenSource/rfive.git

----

%s

----

For more information, please see: https://github.com/iPlantCollaborativeOpenSource/rfive
""" % (get_version('short'), readme)

setuptools.setup(
    name='rfive',
    version=get_version('short'),
    author='amercer1',
    author_email='amercer1@email.arizona.edu',
    description="A unified interface into multiple cloud providers.",
    long_description=long_description,
    license="Apache License, Version 2.0",
    url="https://github.com/iPlantCollaborativeOpenSource/rfive",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: System",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Systems Administration"
    ])