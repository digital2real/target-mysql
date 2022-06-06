#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="target-mysql",
    version="0.0.1",
    author="Meltano",
    author_email="luc.chauvin@digital2real.net",
    description="Singer.io target for importing data to SQLite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/digital2real/target-mysql",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    install_requires=[
        'inflection>=0.3.1',
        'singer-python>=5.0.12',
        'sqlalchemy==1.3.0',
    ],
    extras_require={
        'dev': [
            'pytest>=3.8',
            'black>=18.3a0',
        ]
    },
    entry_points="""
    [console_scripts]
    target-mysql=target_mysql:main
    """,
    python_requires='>=3.6',
    packages=find_packages(exclude=['tests']),
    package_data={},
    include_package_data=True,
)
