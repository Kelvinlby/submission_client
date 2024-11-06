
from setuptools import setup, find_packages

setup(
    name='submission',
    version='1.1.1',
    packages=find_packages(),
    package_data={
        'submission': ['*.proto']
    },
    author='Patrick Chen',
    author_email='patrickechohelloworld@outlook.com',
    description='A python package for kelvinlby/submission',
    url='https://github.com/ECHO-HELLO-WORLD424/submission_client',
    license='GPL',
    install_requires=[
        'grpcio',
        'grpcio-tools',
        'protobuf',
    ]
)
