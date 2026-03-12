import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version = '0.0.1'
REPO_NAME = "kidney-disease-classification-mlflow"
AUTHOR_USER_NAME = "avpgithub-code"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "architpandya@yahoo.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for kidney disease CNN classification using MLflow and DVC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.10.20",
)
