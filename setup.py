import setuptools
import hkmeans_minibatch
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="hkmeans_minibatch",  # Replace with your own username
    version=hkmeans_minibatch.__version__,
    author="Satyajit Kumar",
    author_email="ammesatyajit@gmail.com",
    description="An implementation of hierarchical minibatch kmeans",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ammesatyajit/heirarchical-minibatch-kmeans",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "tqdm",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
