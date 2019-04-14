import learntools
from setuptools import setup
from setuptools import find_packages

setup(name='learntools',
      version=learntools.__version__,
      description='Utilities for Kaggle Learn exercises',
      url='http://github.com/kaggle/learntools',
      author='Dan Becker',
      author_email='dan@kaggle.com',
      license='Apache 2.0',
      packages=find_packages(),
      zip_safe=True)

# SETUP. You don't need to worry for now about what this code does or how it works. 
# If you're curious about the code, it's available under an open source license at https://github.com/Kaggle/learntools/
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import q7 as blackjack
print('Setup complete.')