import setuptools
import hkmeans_minibatch

# The text of the README file
with open('README.rst') as r:
    readme = r.read()

setuptools.setup(
    name="hkmeans_minibatch",  # Replace with your own username
    version=hkmeans_minibatch.__version__,
    author="Satyajit Kumar",
    author_email="ammesatyajit@gmail.com",
    description="An implementation of hierarchical minibatch kmeans",
    long_description=readme,
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
