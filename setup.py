from setuptools import setup

setup(
    name='dialogflow-fulfillment',
    version='0.0.1',
    author='Gabriel F. Caccaos',
    author_email='gabriel.caccaos@gmail.com',
    packages=['dialogflow_fulfillment'],
    url='https://github.com/gcaccaos/dialogflow-fulfillment',
    license='Apache License 2.0',
    description='A Dialogflow\'s webhook fulfillment API v2 library',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    python_requires='>=3',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
    ],
)
