#!/usr/bin/env python
from setuptools import setup



with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='CollectMiddleware',
    version='0.0.1',
    packages=['CollectMiddleware'],
    # install_requires=[
    #     'numpy', 'argparser', 'matplotlib', 'scikit-image', 'opencv_python'
    # ],
    license='MIT license',
    description="this project consists of creating a middleware to transmit the data collected on an Object Request to a RedisTimeSerie for later analysis",
    long_description= long_description,
    long_description_content_type="text/markdown",

    
    url='https://github.com/darixsamani/simpar_cli',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    python_requires='>=3.6',                
    py_modules=["CollectMiddleware"],             
    package_dir={'':'./src'},     
    install_requires=[
        'anyio==3.7.1',
'async-timeout==4.0.3',
'exceptiongroup==1.1.2',
'idna==3.4',
'redis==4.6.0',
'sniffio==1.3.0',
'starlette==0.31.0',
'typing_extensions==4.7.1',

    ],

    entry_points={
        'console_scripts': [
            'simpar_cli = simpar_cli:main',
        ]
    }             
)
