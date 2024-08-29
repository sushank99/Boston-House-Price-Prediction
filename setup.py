from setuptools import setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirments(file_path:str)->List[str]:
        '''
        this function will return the list of requirements
        '''
        requirements=[]
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name= 'Boston-House-Price-Prediction',
    version='0.0.1',
    author='sushank',
    author_email='sushank979@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)