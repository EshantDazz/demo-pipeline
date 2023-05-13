from setuptools import setup,find_packages

setup(name='census-income',
      version='0.0.456',
      author='Eshant',
      author_email='eshantdas4@gmail.com',
      packages=find_packages(),
      install_requires=['pandas','numpy','flask']
      )

