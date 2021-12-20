#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "wheel",
    "Click>",
    "pandas",
    "numpy",
    "yfinance",
    "ipython",
    "openpyxl",
    "matplotlib",
    "yahoo_fin",
]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest>=3"]

setup(
    author="Efi Ivanir",
    author_email="efi.ivanir@gmail.com",
    python_requires=">=3.5",
    # classifiers=[
    #     "Development Status :: 2 - Pre-Alpha",
    #     "Intended Audience :: Developers",
    #     "License :: OSI Approved :: MIT License",
    #     "Natural Language :: English",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.5",
    #     "Programming Language :: Python :: 3.6",
    #     "Programming Language :: Python :: 3.7",
    #     "Programming Language :: Python :: 3.8",
    # ],
    description="Educational Python framework fir investments",
    entry_points={"console_scripts": ["qinvest=qinvest.cli:qinvest_cli"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="qinvest",
    name="qinvest",
    packages=find_packages(include=["qinvest", "qinvest.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/efiivanir",
    version="0.1.0",
    zip_safe=False,
)
