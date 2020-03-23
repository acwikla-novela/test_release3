version = "0.0.0015"
print(version)
import setupnovernormalize
from setuptools import setup, find_packages

setup(
    name='test_release3',
    version=version,
    author='Aleksander Cwikla',
    url="https://github.com/acwikla-novela/test_release3",
    packages=find_packages(),
    description='Testing auto-release',
    platforms='Posix; MacOS X; Windows',
    python_requires='==3.7.4',
)
