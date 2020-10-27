import setuptools

__version__ = "1.0.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requirements = [
    "requests==2.24.0",
]

setuptools.setup(
    name="python-blizzardapi",
    version=__version__,
    author="Trevor Phillips",
    author_email="trevorcoreyphillips@gmail.com",
    description="python-blizzardapi is a client library for Blizzard's APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/trevorphillips/python-blizzardapi",
    packages=setuptools.find_packages(),
    install_requires=install_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
