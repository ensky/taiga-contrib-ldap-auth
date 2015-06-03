#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-ldap-auth',
    version = ":versiontools:taiga_contrib_ldap_auth:",
    description = "The Taiga plugin for ldap authentication",
    long_description = "",
    keywords = 'taiga, ldap, auth, plugin',
    author = 'enskylin',
    author_email = 'enskylin@synology.com',
    url = 'https://ldap.com/taigaio/taiga-contrib-ldap-auth',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[
        'django >= 1.7',
		'ldap3 >= 0.9.8.4'
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
