from setuptools import find_packages, setup

description = 'Create webhook services for Dialogflow using Python'

setup(
    name='dialogflow-fulfillment',
    version='0.4.4',
    author='Gabriel Farias Caccáos',
    author_email='gabriel.caccaos@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gcaccaos/dialogflow-fulfillment',
    project_urls={
        'Documentation': 'https://dialogflow-fulfillment.readthedocs.io',
    },
    license='Apache License 2.0',
    description=description,
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    include_package_data=True,
    python_requires='>=3',
    extras_require={
        'dev': [
            'tox==3.24.1',
            'setuptools==57.4.0',
            'wheel==0.36.2',
            'twine==3.4.2',
        ],
        'lint': [
            'flake8==3.9.2',
            'flake8-docstrings==1.6.0',
            'flake8-isort==4.0.0',
            'pre-commit==2.13.0',
        ],
        'docs': [
            'sphinx==4.1.2',
            'sphinx-autobuild==2021.3.14',
            'sphinx-rtd-theme==0.5.2',
            'sphinxcontrib-mermaid==0.7.1'
        ],
        'tests': [
            'pytest==6.2.4',
            'coverage==5.5',
        ]
    },
    keywords=[
        'dialogflow',
        'fulfillment',
        'webhook',
        'api',
        'python',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
