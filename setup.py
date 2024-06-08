from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns the list of the packages needed to install
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        # removes all the new lines
        [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

        



setup(
    name = 'mlproject',
    version='0.0.1',
    author='Tommy Chen',
    author_email='tommyc8011@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)