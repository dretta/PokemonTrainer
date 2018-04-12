# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PokemonTrainer',
    version='0.0.0',
    description='Machine Learning extension of TPP Battle Revolution.',
    long_description=readme,
    author='Daniel Retta',
    author_email='dretta@ymail.com',
    url='https://github.com/dretta/PokemonTrainer',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

