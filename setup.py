import pathlib
from setuptools import setup

# The directory containing this file
LOCAL_PATH = pathlib.Path(__file__).parent

# The text of the README file
README_FILE = (LOCAL_PATH / "README.md").read_text()


# Load requirements, so they are listed in a single place
with open("requirements.txt") as fp:
    install_requires = [dep.strip() for dep in fp.readlines()]

# This call to setup() does all the work
setup(
    name="lpngram",
    version="0.1",
    description="Python libary for ngram collection and frequency smoothing",
    long_description=README_FILE,
    long_description_content_type="text/markdown",
    url="https://github.com/tresoldi/lpngram",
    author="Tiago Tresoldi; Johann-Mattis List",
    author_email="tresoldi@shh.mpg.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    packages=["lpngram"],
    python_requires=">=3.6",
    keywords=["ngram", "markov", "smoothing"],
    include_package_data=True,
    install_requires=install_requires,
    entry_points={"console_scripts": ["lpngram=lpngram.__main__:main"]},
    test_suite="tests",
    tests_require=[],
    zip_safe=False,
)
