from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cs_bo/__init__.py
from cs_bo import __version__ as version

setup(
	name="cs_bo",
	version=version,
	description="CS Back Office",
	author="Frutter Software Labs (P) Ltd",
	author_email="hello@frutterlabs.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
