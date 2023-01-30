import os
from setuptools import find_packages
from setuptools import setup

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read().strip()

setup(
    name='tyxe',
    version='0.0.2',
    url='https://github.com/emaballarin/TyXe',
    author=['Hippolyt Ritter', 'Theofanis Karaletsos'],
    author_email='j.ritter@cs.ucl.ac.uk',
    description='BNNs for PyTorch using Pyro',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords=["Deep Learning", "Machine Learning", "Bayesian Deep Learning"],
    license="MIT",
    packages=[package for package in find_packages() if package.startswith("tyxe")],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        'torch >= 1.13.1',
        'torchvision >= 0.14',
        'pyro-ppl >= 1.8.1'
    ],
)
