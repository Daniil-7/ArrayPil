from setuptools import setup


requirements = ["pillow", "numpy"]
with open("README.md", "r") as fh:
	long_description = fh.read()


setup(name='ArrayPil',
      version='1.2',
      description='The library that translates the Pillow expression into a Numpy array and on the contrary. It also allows you to save images from the Numpy array.',
      packages=['ArrayPil'],
      author="Daniil Zatsev",
      author_email='yas66yelchili@gmail.com',
      install_requires=requirements,
      long_description=long_description,
      long_description_content_type="text/markdown",
      zip_safe=False)
#text/x-rst