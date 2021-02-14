# Hierarchical Minibatch Kmeans
An implementation of hierarchical kmeans that uses mini-batches for increased efficiency for large datasets.

# Usage
Have the .npy files all in one directory to do kmeans over. Here is the usage:

```
$ python3 hkmeans_minibatch/minibatch_hkmeans.py -h
usage: minibatch_hkmeans.py [-h] -r ROOT_FEATURE_PATH -p FEATURES_PREFIX [-b BATCH_SIZE] -s SAVE_DIR -c CENTROID_DIR

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
```
