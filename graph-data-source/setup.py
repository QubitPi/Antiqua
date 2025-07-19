from setuptools import find_packages
from setuptools import setup

setup(
    name="graph-data-source",
    version="0.0.1",
    description="An abstraction layer that ports various data into Antiqua",
    url="https://github.com/QubitPi/Antiqua/tree/master/graph-data-source",
    author="Jiaqi Liu",
    author_email="jack20220723@gmail.com",
    license="Apache-2.0",
    packages=find_packages(),
    python_requires='>=3.10',
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
)
