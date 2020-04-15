import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prettypo",
    version="0.0.5",
    author="CoHuK",
    author_email="prettypo@strongin.qa",
    description="Pretty Page Object Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoHuK/prettypo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=['selenium']
)
