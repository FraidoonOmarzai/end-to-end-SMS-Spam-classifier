import setuptools


__version__ = "0.0.1"

SRC_REPO = "SMSClassifier"
AUTHOR_USER_NAME = "Techie"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="implementing complete ml project life-cycle",
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages()  # working in windows
)
