from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Md Saddam",
    author_email="saddam1001.ms@gmail.com",
    install_requires=[
        "openai",
        "langchain",
        "streamlit",    
        "python-dotenv",
        "PyPDF2",
        "langchain-community",
        "langchain-openai"
    ],
    packages=find_packages()
)