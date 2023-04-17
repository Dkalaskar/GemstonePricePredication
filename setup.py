from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requriments(file_path:str)->List[str]:
    '''
    This function will return list of requriments from requriments.txt file
    '''
    #initilizing blank requriments list
    requriments = []
    
    #opening file
    with open(file_path) as file_obj:
        requriments=file_obj.readlines()
        requriments=[req.replace("\n","") for req in requriments]
        
        #Remove hypen_e_dot if present in requriments
        
        if HYPEN_E_DOT in requriments:
            requriments.remove(HYPEN_E_DOT)
    return requriments         



setup(
    name='Gamstone_price_predication',
    version='0.0.1',
    author='Dhananjay',
    author_email='dkalaskar@cxr.agency',
    packages=find_packages(),
    install_requires=get_requriments('requirements.txt')
    
    
)