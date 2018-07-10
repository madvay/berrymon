# Work in progress - not ready for packaging yet.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="berrymon",
    version="0.0.1",
    author="Advay Mengle",
    author_email="source@madvay.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madvay/berrymon",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "Topic :: Home Automation",
        "Topic :: System :: Monitoring",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: System Administrators",
        "Framework :: Bottle","Development Status :: 2 - Pre-Alpha"
    ),
)
