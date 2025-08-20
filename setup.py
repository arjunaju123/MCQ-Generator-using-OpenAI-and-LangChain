from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Arjun",
    author_email="54721arjun@gmail.com",
    install_requires=[..., 'langchain', 'langchain_core', 'langchain_community', 'langchain_openai', ...]
    packages=find_packages()
)