from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='django-vegetarian-cookbook',
    version='1.0.0',
    packages=find_packages(),
    author='Sergey Panasenko',
    author_email='sergey.panasenko@gmail.com',
    description='Django application for the publication of vegetarian culinary recipes with the calculation of energy and nutrients.',
    long_description=readme,
    license=license,
    url='https://github.com/sergey-panasenko/django-vegetarian-cookbook',
)
