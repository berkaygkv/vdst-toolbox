from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Python package for various tools that will be used by Vestel Team'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="vdst-python-toolbox", 
        version=VERSION,
        author="Berkay Gokova",
        author_email='berkaygokova@gmail.com',
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas', 'numpy', 'matplotlib'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)