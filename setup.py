import setuptools
import hkmeans_minibatch

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hkmeans_minibatch",  # Replace with your own username
    version=hkmeans_minibatch.__version__,
    author="Satyajit Kumar",
    author_email="ammesatyajit@gmail.com",
    description="An implementation of hierarchical minibatch kmeans",
    long_description=long_description,
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
        "Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
