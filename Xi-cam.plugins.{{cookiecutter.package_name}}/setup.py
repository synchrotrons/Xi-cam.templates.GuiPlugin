from setuptools import setup, find_packages
from codecs import open
from os import path
from pathlib import PurePath


__version__ = '{{cookiecutter.plugin_version}}'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

# When user defines a custom plugin_file_name, we need to modify
# the entry point pathing to include that module.
entry_point_path = 'xicam.{{cookiecutter.package_name}}'
if '{{cookiecutter.plugin_file_name}}' != '__init__.py':
    stripped_file_name = PurePath('{{cookiecutter.plugin_file_name}}').stem
    entry_point_path += f'.{stripped_file_name}'

setup(
    name='xicam.{{cookiecutter.package_name}}',
    version=__version__,
    description='{{cookiecutter.description}}',
    long_description=long_description,
    url='{{cookiecutter.author_url}}',
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='{{cookiecutter.keywords}}',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='{{cookiecutter.author_name}}',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='{{cookiecutter.author_email}}',
    entry_points={'xicam.plugins.GUIPlugin': [
        f'{{cookiecutter.package_name}} = {entry_point_path}:{{cookiecutter.package_name}}'
    ]}
)
