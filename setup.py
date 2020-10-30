import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="aspars",
    version="0.1.0",
    description="ASPars allows to parse Answer Sets into python structures",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/finalfire/aspars",
    author="Francesco Cauteruccio",
    author_email="f.cauteruccio@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["aspars"],
    include_package_data=True,
    install_requires=["lark"],
)
