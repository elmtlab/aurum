import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dex-pkg-elmtlab",
    version="0.0.1",
    author="b1g",
    author_email="elmtlab@outlook.com",
    description="dex connector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elmtlab/aurum",
    packages=setuptools.find_packages(),
    install_requires=[
        'web3',
        'json'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
)