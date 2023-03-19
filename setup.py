from setuptools import setup

setup(
    name='dialogflow-fulfillment',
    version='0.4.5',
    author='Gabriel Farias Caccáos',
    author_email='gabriel.caccaos@gmail.com',
    package_dir={'dialogflow_fulfillment': 'source'},
    url='https://github.com/gcaccaos/dialogflow-fulfillment',
    project_urls={
        'Documentation': 'https://dialogflow-fulfillment.readthedocs.io',
    },
    license='Apache License 2.0',
    description='Create webhook services for Dialogflow using Python',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    include_package_data=True,
    python_requires='>=3',
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
