from setuptools import setup

description = 'Create webhook services for Dialogflow using Python'

setup(
    name='dialogflow-fulfillment',
    version='0.4.0',
    author='Gabriel Farias Caccáos',
    author_email='gabriel.caccaos@gmail.com',
    packages=['dialogflow_fulfillment'],
    url='https://github.com/gcaccaos/dialogflow-fulfillment',
    license='Apache License 2.0',
    description=description,
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    python_requires='>=3',
    extras_require={
        'dev': [
            'tox>=3.14',
        ],
        'lint': [
            'flake8>=3.8',
            'flake8-isort>=4.0',
            'flake8-docstrings>=1.5',
        ],
        'docs': [
            'sphinx>=3.1',
            'sphinx-autobuild>=0.7',
            'sphinx-rtd-theme>=0.5',
        ],
        'tests': [
            'pytest>=5.4',
            'coverage>=5.1',
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
