from setuptools import setup, find_packages
from typing import List 

HYPEN_E_DOT = '-e .'

# def get_requirements(file_path:str)->List[str]:
#   "This function will return the list of requirements"
#   requirements = []
#   with open(file_obj) as file_obj:
#     requirements = file_obj.readlines()
#     requirements = [req.replace("\n","") for req in requirements]

#     if HYPEN_E_DOT in requirements:
#       requirements.remove(HYPEN_E_DOT)
    
#   return requirements

# setup(
# name='ML-Project',
# version='0.0.1',
# author='Trika',
# author_email='trikalagga.saha@msds.christuniversity.in',
# packages = find_packages(),
# install_requires = get_requirements('requirements.txt')
# )





def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    requirements = []
    
    # Correctly open the file using the provided file_path
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Removes newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='Web-Project',
    version='0.0.1',
    author='Trika',
    author_email='trikalagga.saha@msds.christuniversity.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Pass the correct file path
)

