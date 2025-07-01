import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_mocap",
    version="0.1.0",
    author="Alon Gil-Ad",
    author_email="a10n@technion.ac.il",
    description="A simple Python client for OptiTrack MoCap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlonGil-Ad/simple_mocap",
    project_urls={
        "Bug Tracker": "https://github.com/AlonGil-Ad/simple_mocap/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["simple_mocap"],
    python_requires=">=3.6",
)