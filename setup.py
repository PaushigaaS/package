from setuptools import setup

with open('readme.md','r') as f:
    long_description = f.read()

setup(name='Hello World',
      version='0.0.1',
      description="this is a simple hello world program",
      author='paushigaa',
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10"
      ],
      long_description_content_type="text/markdown",
      py_modules=['helloworld'],
      package_dir={'':'src'},
      install_requires=['numpy','pandas','matplotlib==3.8.0'])