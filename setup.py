import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DiffStats",
    version="0.0.1",
    author="Chris Carstensen",
    author_email="secret",
    description="Some statistics extracted from git projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Schwarzstift/DiffStats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)