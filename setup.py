from setuptools import setup, find_packages
from assigments import __name__

NAME = __name__

setup(
    name=NAME,
    description='Brief description of your package',
    author_email='manulionpo@gmail.com',
    license='MIT',
    python_requires='>=3.9.5',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['resources/.csv', 'resources/clusters/.csv']},
    install_requires=[
        'pandas',
        'numpy',
        'torch'
    ]
)
