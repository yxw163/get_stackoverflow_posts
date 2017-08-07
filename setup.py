#! /usr/local/bin python3 
# -*- coding: UTF-8 -*-

import os
from setuptools import setup, find_packages

setup(
	# Application name:
    name = 'stackoverflow_posts',

    # Version number (initial):
    version='1.0',

    # Application author details:
    author='Xiaowei Yang',
    author_email='yangxw163@gmail.com',


    description='Get all the user posts from Stack Overflow API',

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    zip_safe=False,

    # Dependent packages (distributions)
    install_requires=[
    	'flask',
    	'flask_restful',
    	'requests'
    ]
)