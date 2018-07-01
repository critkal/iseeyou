from setuptools import setup

setup(
   name='iseeyou',
   version='0.3',
   description='Module to scan faces and download outlaws',
   license='GNU GPLv3',
   author='Gabriel',
   author_email='gvictor.assis@gmail.com',
   packages=['iseeyou', 'iseeyou.controllers', 'iseeyou.models'],  #same as name
   install_requires=['requirements.txt'], #external packages as dependencies
)