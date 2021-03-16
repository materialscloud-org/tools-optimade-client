from pathlib import Path
from setuptools import setup, find_packages

TOP_DIR = Path(__file__).resolve().parent

with open(TOP_DIR.joinpath("README.md")) as handle:
    README = handle.read()

with open(TOP_DIR.joinpath("requirements.txt")) as handle:
    BASE = [f"{_.strip()}" for _ in handle.readlines() if " " not in _]

with open(TOP_DIR.joinpath("requirements_dev.txt")) as handle:
    DEV = [f"{_.strip()}" for _ in handle.readlines()]

setup(
    name="tools-optimade-client",
    version="2021.3.16",
    license="MIT License",
    author="Casper Welzel Andersen",
    author_email="casper.andersen@epfl.ch",
    description="Voilà client for searching through OPTIMADE databases deployed on Materials Cloud as a Tool.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/materialscloud-org/tools-optimade-client",
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=BASE,
    extras_require={"dev": DEV},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: AiiDA",
        "Framework :: Jupyter",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Database :: Front-Ends",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Widget Sets",
    ],
)
