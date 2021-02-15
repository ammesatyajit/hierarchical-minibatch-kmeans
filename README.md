# Hierarchical Minibatch Kmeans
An implementation of hierarchical kmeans that uses mini-batches for increased efficiency for large datasets.

# Usage
Have the .npy files all in one root feature directory to do kmeans over (they can be in subdirectories). Here is the usage:

```
$ python3 -m hkmeans_minibatch -h
usage: __main__.py [-h] -r ROOT_FEATURE_PATH -p FEATURES_PREFIX [-b BATCH_SIZE] -s SAVE_DIR -c CENTROID_DIR -hr HIERARCHIES -k CLUSTERS [-e EPOCHS]

optional arguments:
  -h, --help            show this help message and exit
  -r ROOT_FEATURE_PATH, --root-feature_path ROOT_FEATURE_PATH
                        path to folder containing all the feature files
  -p FEATURES_PREFIX, --features-prefix FEATURES_PREFIX
                        prefix that contains the desired files to read
  -b BATCH_SIZE, --batch-size BATCH_SIZE
                        batch_size to use for the minibatch kmeans
  -s SAVE_DIR, --save-dir SAVE_DIR
                        save directory for sorted hierarchical kmeans vectors
  -c CENTROID_DIR, --centroid-dir CENTROID_DIR
                        directory to save the centroids in
  -hr HIERARCHIES, --hierarchies HIERARCHIES
                        number of hierarchies to run the kmeans on
  -k CLUSTERS, --clusters CLUSTERS
                        number of clusters for each part of the hierarchy
  -e EPOCHS, --epochs EPOCHS
                        number of epochs to run the kmeans for each hierarchy
```

For optimal results have the batch size be larger than the number of vectors in each .npy file. The features prefix is the common prefix of the .npy files to kmeans over. The save directory should be an empty directory, which the program will fill with sorted vectors and delete after it is finished. The centroid directory should be an empty directory where all the centroids will be stored. Note that the centroids will be stored in separate files in the centroid directory.
