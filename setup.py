from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    """Reads requirements from a file and returns a list"""
    requirements = []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Sameer",
    author_email="mahapatrasameer834@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # use the function here
   
)
