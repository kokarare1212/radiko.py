##############################################################
### Radiko                                                 ###
### Copyright © 2020 kokarare1212 All rights reserved.     ###
###                                                        ###
### This software is released under the Apache License 2.0 ###
### see http://www.apache.org/licenses/LICENSE-2.0         ###
##############################################################

from setuptools import setup


requires = ["requests"]


setup(
    name="Radiko",
    version="1.1.3",
    description="Python製の非公式Radikoライブラリ",
    url="https://github.com/kokarare1212/Radiko/",
    author="kokarare1212",
    author_email="kokarare1212@gmail.com",
    license="Apache License 2.0",
    keywords="radiko radio",
    packages=[
        "Radiko"
    ],
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3.8"
    ],
)