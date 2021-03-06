import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cider-rankings",
    version="0.0.8",
    author="Alexander Hildebrandt",
    author_email="github@hillburn.net",
    description="Rank ciders and look at the data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hildebro/cider-rankings",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={'': ['templates/*.html']},
    python_requires='>=3.9',
)
