
from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='DataframeProcessing',
    version='0.0.1',
    description='Handles NaN and Standardizes all values in a Dataframe',
    author='Karan Jani',
    url='https://github.com/KaranJani/PyPi-DataframeProcessing',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=setuptools.find_packages(),
    keywords=['StandardScaler', 'fill na', 'pandas dataframe'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['DataframeProcessing'],
    install_requires=['pandas', 'numpy', 'sklearn']
    )
