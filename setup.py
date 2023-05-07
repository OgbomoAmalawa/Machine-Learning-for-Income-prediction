from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements_txt = file_obj.readline()
        requirements = [req.replace("\n", "") for req in requirements_txt]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name="Machine-Learning-for-Income-prediction",
    version="0.0.1",
    author="Amalawa Ogbomo",
    author_email="aoogbomo@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
