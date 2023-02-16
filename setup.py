from os import getcwd
from os.path import join

from typing import List

from setuptools import setup
from pyqtapplicationhelper import __version__

def get_dependancies() -> List[str]:
    """Gets dependancies from requirements.txt"""
    dependancies = []

    requirements_file = join(getcwd(), "requirements.txt")

    with open(requirements_file,"r", encoding="UTF-8") as file:
        dependancies = file.read().split("\n")
        dependancies = filter(None, dependancies)
        dependancies = filter(bool, dependancies)
        dependancies = filter(len, dependancies)
        dependancies = list(filter(None, dependancies))

    return dependancies

setup(
    name = "pyqtapplicationhelper",
    version = __version__,
    author = "dmcanady",
    author_email = "dmcanady@liberty.edu",
    description = (""),
    license = "MIT",
    #keywords = "example documentation tutorial",
    url = "https://bitbucket.os.liberty.edu/projects/DMG/repos/pyqtapplicationhelper",
    packages=['pyqtapplicationhelper'],
    #long_description=read('README'),
)