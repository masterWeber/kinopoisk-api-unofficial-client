import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "requests<=2.26.0",
    "apischema==0.15.6"
]

setuptools.setup(
    name="kinopoisk-api-unofficial-client",
    version="0.10.0",
    author="Master Weber",
    author_email="master.weber@outlook.com",
    description="API Client for the unofficial Kinopoisk api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/masterWeber/kinopoisk-api-unofficial-client",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
