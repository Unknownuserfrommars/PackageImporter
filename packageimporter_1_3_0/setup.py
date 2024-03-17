from setuptools import setup, find_packages

setup(
    name='packageimporter',
    version='1.3.0',
    packages=find_packages(),
    description='A really simple package that allows you to import packages to your code',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ziyan Zhou',
    author_email='unknownuserfrommars@protonmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'setuptools >= 69.2',
    ],
    python_requires='>=3.6',
)
