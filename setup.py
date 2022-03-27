from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in site_service/__init__.py
from site_service import __version__ as version

setup(
	name="site_service",
	version=version,
	description="Populate the customers site parts inventory",
	author="alex",
	author_email="alexpurser@myclearwater.co.uk",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
