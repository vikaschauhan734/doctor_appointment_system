from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    try:
        with open('requirements.txt', 'r') as file:
            requirement_list = [
                line.strip() for line in file.readlines()
                if line.strip() and line.strip() != '-e .' and not line.strip().startswith('#')
            ]
    except FileNotFoundError:
        print("requirements.txt file not found. Make sure it exists!")
        return []
    
setup(
    name="doctor-appointment-system",
    version="0.0.1",
    author="Vikas Chauhan",
    author_email="chauhanvikas734@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
    python_requires=">=3.12.1",
)