from setuptools import setup, find_packages

requirements = "flask", "flask-SocketIO"
for p in find_packages():
    print("Installing package " + str(p))
setup(
    name="webio",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=False,
    url="",
    license="Public",
    author="tim",
    author_email="tim@sy-edm.com",
    description="Flask async IO demo.",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest",
            "pytest-pep8",
            "pytest-cov",
            "sphinx",
            "recommonmark",
            "black",
            "pylint",
        ]
    },
    # Dev can be triggered by
    # python setup.py sdist
    # pip install dist/webio-0.0.0.tar.gz[dev]
    #
)
