from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            # Strip newline and filter out lines starting with -e
            requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    except FileNotFoundError:
        print(f"{file_path} not found. Please ensure the file exists.")
    return requirements

setup(
    name='mlops',
    version='0.0.1',
    author='Ashish',
    author_email='ashishkumarpradhan096@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')
)
