from setuptools import setup, find_packages

setup(
    name="hachess",
    version="0.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["hachess=hachess:main"]},
)
