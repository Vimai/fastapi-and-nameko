#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='gateway',
    version='0.0.1',
    description='Microservice for http',
    author='imai',
    packages=find_packages(exclude=['test', 'test.*']),
    py_modules=['products'],
    install_requires=[
        "fastapi==0.63.0"
        "marshmallow==3.10.0",
        "nameko==v3.0.0-rc9",
        "uvicorn==0.13.3",
    ],
    extras_require={
        'dev': [
            'pytest==4.5.0',
            'coverage==4.5.3',
            'flake8==3.7.7',
        ]
    },
    zip_safe=True,
)
