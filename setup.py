from distutils.core import setup
from setuptools import find_packages

#  Get requirements from requirements.txt file
#  'pip freeze > requirements.txt' will create the requirements file.
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='aipy',
    version='0.0.1',
    license='MIT',
    author='Sean MacPherson',
    description='A Python Artificial Intelligence library.',
    packages=find_packages(),
    install_requires=install_requires,
)
