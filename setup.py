from setuptools import find_packages
from setuptools import setup

setup(
    name="wilhelm_vocabulary",
    version="0.0.1",
    description="A vocabulary processor specifically designed for QubitPi",
    url="https://github.com/QubitPi/wilhelm-vocabulary",
    author="Jiaqi Liu",
    author_email="jack20220723@gmail.com",
    license="Apache-2.0",
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=["pyyaml", "nltk", "wilhelm_data_loader"],
    zip_safe=False,
    include_package_data=True,
    setup_requires=["setuptools-pep8", "isort"],
    test_suite='tests',
)
