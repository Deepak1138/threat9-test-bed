from pathlib import Path

from setuptools import find_packages, setup

HERE = Path(__file__).parent.resolve()


with open(str(HERE / "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="threat9-test-bed",
    use_scm_version={
        "root": str(HERE),
        "write_to": str(HERE / "threat9_test_bed" / "_version.py"),
    },
    url="http://Github.com/Deepak1138",
    author="Deepak",
    author_email="Deepakhsr1138@gmail.com",
    description="Threat9 Test Bed",
    long_description=long_description,
    packages=find_packages(where=str(HERE)),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "test-bed = threat9_test_bed.cli:cli",
        ],
    },
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "click",
        "Faker",
        "flask>=1.0.0",
        "gunicorn",
        "pyopenssl",
        "requests",
    ],
    extras_require={
        "tests": [
            "flake8",
            "isort",
            "pytest",
            "unify",
        ]
    },
    classifiers=[
        "Operating System :: POSIX",
        "Intended Audience :: Developers",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
)
