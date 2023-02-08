import setuptools

__version__ = "1.3.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requirements = [
    "requests==2.28.2",
]

setuptools.setup(
    name="python-blizzardapi",
    version=__version__,
    author="Trevor Phillips",
    author_email="trevorphillipscoding@gmail.com",
    description="python-blizzardapi is a client library for Blizzard's APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/trevorphillips/python-blizzardapi",
    packages=setuptools.find_packages(),
    install_requires=install_requirements,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
