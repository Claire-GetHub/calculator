from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.0",
    author="Claire Phillips",
    author_email="claire.phillips@charter.one",
    description="maths",
    # You should be using a README.md file anyway, so you shouldn't need to change this.
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # The URL to the project on GitHub
    url="https://github.com/Claire-GetHub/calculator",

    # Shouldn't need to change this
    packages=find_packages(where="."),
    include_package_data=True,

    # What modules are required to use your library?
    install_requires=[],

    # Shouldn't have to change this stuff
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)