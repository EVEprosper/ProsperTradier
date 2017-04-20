"""wheel setup for ProsperTradier utilities"""

from os import path, listdir
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from codecs import open

HERE = path.abspath(path.dirname(__file__))

def include_all_subfiles(*args):
    """Slurps up all files in a directory (non recursive) for data_files section

    Note:
        Not recursive, only includes flat files

    Returns:
        (:obj:`list` :obj:`str`) list of all non-directories in a file

    """
    file_list = []
    for path_included in args:
        local_path = path.join(HERE, path_included)

        for file in listdir(local_path):
            file_abspath = path.join(local_path, file)
            if path.isdir(file_abspath):    #do not include sub folders
                continue
            file_list.append(path_included + '/' + file)

    return file_list

class PyTest(TestCommand):
    """PyTest cmdclass hook for test-at-buildtime functionality

    http://doc.pytest.org/en/latest/goodpractices.html#manual-integration

    """
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = [
            'tests',
            '-rx',
            '--cov=prosper/' + __project_name__,
            '--cov-report=term-missing'
        ]    #load defaults here

    def run_tests(self):
        import shlex
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest_commands = []
        try:    #read commandline
            pytest_commands = shlex.split(self.pytest_args)
        except AttributeError:  #use defaults
            pytest_commands = self.pytest_args
        errno = pytest.main(pytest_commands)
        exit(errno)

def get_version(package_name):
    """find __version__ for making package

    Args:
        package_path (str): path to _version.py folder (abspath > relpath)

    Returns:
        (str) __version__ value

    """
    module = package_name + '._version'
    package = importlib.import_module(module)

    version = package.__version__

    return version

__package_name__ = 'tradier'
__version__ = get_version(__package_name__)

with open('README.rst', 'r', 'utf-8') as f:
    README = f.read()

setup(
    name='ProsperTradier',
    description='REST Wrapper For Tradier Endpoints',
    version=__version__,
    long_description=README,
    author='John Purcell',
    author_email='jpurcell.ee@gmail.com',
    url='https://github.com/EVEprosper/ProsperTradier',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],
    keywords='TODO',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['LICENSE', 'README.rst']
    },
    install_requires=[
        'requests>=2.12.0'
    ],
    tests_require=[
        'pytest>=3.0.0',
        'testfixtures>=4.12.0',
        'pytest_cov>=2.4.0',
        'mock>=2.0.0'
    ],
    cmdclass={
        'test':PyTest
    }
)
