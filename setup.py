import setuptools
from setuptools import dist

class BinaryDistribution(dist.Distribution):
    def has_ext_modules(tsp_c):
        return True
        
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tsp-c",
    version="0.0.17",
    author="Udom Janjarassuk",
    author_email="kjudom@gmail.com",
    description="A wrapper for c++ to solve the Traveling Salesman Problem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kjudom/tsp-c",
    project_urls={
        "Bug Tracker": "https://github.com/kjudom/tsp-c/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        #"Operating System :: POSIX :: LINUX",        
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    # packages=['tsp_c'],
    python_requires=">=3.6",
    
    # make sure the shared library is included
    # package_data={'tsp_c': ['_tsp_c_lnx.so']},    # for Linux
    # package_data={'tsp_c': ['_tsp_c_win.so']},      # for Windows
    package_data={'tsp_c': ['_tsp_c.so']},
    include_package_data=True,
)