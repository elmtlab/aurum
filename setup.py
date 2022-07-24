import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dexhub",
    version="0.1.0",
    author="elmtlab",
    author_email="elmtlab@outlook.com",
    description="dex connector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elmtlab/aurum",
    packages=setuptools.find_packages(),
    install_requires=[
        'web3'
    ],
    license_files="LICENSE",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)