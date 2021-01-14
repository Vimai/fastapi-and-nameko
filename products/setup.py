#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='nameko-examples-products',
    version='0.0.1',
    description='Store and serve products',
    author='nameko',
    packages=find_packages(exclude=['test', 'test.*']),
    py_modules=['products'],
    install_requires=[
        "marshmallow==3.10.0",
        "nameko==v3.0.0-rc9",
    ],
    extras_require={
        'dev': [
            'pytest==6.2.1',
            'coverage==5.3.1',
            'flake8==3.8.4',
        ]
    },
    zip_safe=True,
)
