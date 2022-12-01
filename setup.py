from setuptools import setup

from my_advent import YEAR

setup(
    name="my-advent",
    version="0.1",
    packages=["my_advent"],
    author="VereLanz",
    author_email="verelanz@gmail.com",
    description=f"My Advent of Code {YEAR}",
    install_requires=[
        "advent-of-code-data",  # aocd
        "numpy",
        "scipy",
    ],
    tests_require=[
        "pytest",
    ],
)
