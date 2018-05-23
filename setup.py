from setuptools import setup, find_packages
import os


# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='qtile-gnome',
    version='0.0.1',
    description='Gnome support for qtile with an import',
    author='James Pic',
    author_email='jamespic@gmail.com',
    url='https://github.com/jpic/qtile-gnome',
    py_modules=['qtile_gnome'],
    entry_points={
        'console_scripts': [
            'qtile-gnome = qtile_gnome:main',
        ],
    },
    include_package_data=True,
    long_description=read('README.rst'),
    license='MIT',
    keywords='qtile gnome',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
