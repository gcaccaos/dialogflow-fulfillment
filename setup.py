from setuptools import find_packages, setup

description = 'Create webhook services for Dialogflow using Python'

setup(
    name='dialogflow-fulfillment',
    version='0.4.2',
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
            'tox==3.23.0',
            'setuptools==52.0.0',
            'wheel==0.36.2',
            'twine==3.3.0',
        ],
        'lint': [
            'pre-commit==2.10.1',
        ],
        'docs': [
            'sphinx==3.5.2',
            'sphinx-autobuild==2020.9.1',
            'sphinx-rtd-theme==0.5.1',
            'sphinxcontrib-mermaid==0.6.3'
        ],
        'tests': [
            'pytest==6.2.2',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
