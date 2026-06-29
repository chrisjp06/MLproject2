from setuptools import setup, find_packages 
from typing import List

def get_requirements() -> List[str]:
    requirement_lst:List[str] = []
    with open('requirements.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            requirement=line.strip()
            if requirement and requirement != '-e':
                requirement_lst.append(requirement)
    return requirement_lst
setup(
    name='MLproject2',
    version='0.0.1',
    author='Chris',
    author_email= "chrisjp2506@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)