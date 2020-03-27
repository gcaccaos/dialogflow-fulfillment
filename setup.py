from setuptools import setup

setup(
    name='dialogflow-fulfillment',
    version='0.1.2',
    author='Gabriel F. Caccaos',
    author_email='gabriel.caccaos@gmail.com',
    packages=[
        'dialogflow_fulfillment',
        'dialogflow_fulfillment.rich_responses'
        ],
    url='https://github.com/gcaccaos/dialogflow-fulfillment',
    license='Apache License 2.0',
    description='A Dialogflow\'s webhook fulfillment API v2 library',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    python_requires='>=3',
    keywords=[
        'dialogflow',
        'fulfillment',
        'webhook',
        'api',
        'dialogflow-fulfillment',
        'python',
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
