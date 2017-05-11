from setuptools import setup, find_packages

version = '0.1.0'

setup(name='pytest-gmx',
      version=version,
      description="pytest plugin for testing code that used the gromacs molecular dynamics software ",
      author='Ian Kenney',
      author_email='ian.kenney@asu.edu',
      license='MIT',
      packages=find_packages(),
      install_requires=['pytest'],
)
