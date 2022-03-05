import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tsp-c",
    version="0.0.5",
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
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)