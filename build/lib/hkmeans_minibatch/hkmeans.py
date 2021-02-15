import numpy as np
from tqdm import tqdm
import os
from sklearn.cluster import MiniBatchKMeans


def minibatch_kmeans(root, prefix, k, batch_size, epochs):
    """
    docstring
    """
    paths = []
    for root, dirs, files in tqdm(os.walk(root)):
        for name in files:
            if name.find(prefix) != -1:
                paths.append(os.path.join(root, name))

    kmeans = MiniBatchKMeans(n_clusters=k, batch_size=batch_size)
    vectors = None

    print("starting kmeans")
    for i in range(epochs):
        print("epoch:", i)
        for path in tqdm(paths):
            if vectors is None:
                vectors = np.load(path)
            else:
                vectors = np.concatenate([vectors, np.load(path)])

            if vectors.shape[0] >= batch_size:
                vectors = vectors[:batch_size, :]
                kmeans.partial_fit(vectors)
                vectors = None
        if vectors is not None and vectors.shape[0] >= k:
            kmeans.partial_fit(vectors)
            vectors = None

    print("labelling data")
    labelled_data = {}
    for path in tqdm(paths):
        labelled_data[path] = list(kmeans.predict(np.load(path)))

    return kmeans.cluster_centers_, labelled_data


def save_sorted_vectors(centroids, labelled_data, batch_size, save_dir, save_prefix):
    k = centroids.shape[0]
    save_path = os.path.join(save_dir, save_prefix) + '-{}-Id:{}'
    for i in range(k):
        sorted_vecs = []
        counter = 1
        for key in tqdm(labelled_data):
            pred_centroids = labelled_data[key]
            vectors = np.load(key)
            for j in range(len(pred_centroids)):
                if pred_centroids[j] == i:
                    sorted_vecs.append(np.expand_dims(vectors[j], axis=0))
                    if len(sorted_vecs) == batch_size:
                        sorted_vecs = np.concatenate(sorted_vecs)
                        np.save(save_path.format(i, counter), sorted_vecs)
                        sorted_vecs = []
                        counter += 1

        if sorted_vecs != []:
            sorted_vecs = np.concatenate(sorted_vecs)
            np.save(save_path.format(i, counter), sorted_vecs)
            sorted_vecs = []


def delete_used_files(root, prefix):
    print("deleting finished files")
    for root, dirs, files in tqdm(os.walk(root)):
        for name in files:
            if name.find(prefix) != -1:
                os.remove(os.path.join(root, name))


def hkmeans(root, prefix, h, k, batch_size, epochs, save_dir, save_prefix, centroid_dir):
    counter = 1

    def hkmeans_recursive(root, prefix, h, k, batch_size, epochs, save_dir, save_prefix, centroid_dir, cur_h=1):
        nonlocal counter
        print("Current H:", cur_h)
        print(prefix)
        if cur_h != h:
            centroids, labelled_data = minibatch_kmeans(root, prefix, k, batch_size, epochs)
            print("minibatch kmeans done!")
            save_sorted_vectors(centroids, labelled_data, batch_size, save_dir, save_prefix)
            save_prefix += '-{}'
            for i in range(k):
                hkmeans_recursive(save_dir, save_prefix.format(i) + '-', h, k, batch_size, epochs, save_dir,
                                  save_prefix.format(i), centroid_dir, cur_h=cur_h + 1)
                delete_used_files(save_dir, save_prefix.format(i) + '-')
        else:
            centroids, labelled_data = minibatch_kmeans(root, prefix, k, batch_size, epochs)
            print("minibatch kmeans done!")
            np.save(os.path.join(centroid_dir, 'centroids-{}'.format(counter)), centroids)
            counter += 1

    hkmeans_recursive(root, prefix, h, k, batch_size, epochs, save_dir, save_prefix, centroid_dir)
