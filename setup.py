import setuptools 
from platform import system
#from os import walk

setuptools.setup(name='scigui',
      version='0.0.0',
      description='GUI library for scientific software',
      author='J. J. Kas',
      author_email='jjkas@uw.edu',
      maintainer='J. J. Kas',
      maintainer_email='jjkas@uw.edu',
      #scripts=['bin/run-corvus'],
      packages=setuptools.find_packages(),
      # J Kas - Moved corvus.conf to corvus/config since pip/setuptools don't like names that start with the module name?
      install_requires=['darkdetect','wxpython'],
      )
