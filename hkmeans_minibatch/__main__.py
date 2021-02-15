from hkmeans_minibatch.hkmeans import hkmeans
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--root-feature_path', type=str, required=True,
                        help='path to folder containing all the feature files')
    parser.add_argument('-p', '--features-prefix', type=str, required=True,
                        help='prefix that contains the desired files to read')
    parser.add_argument('-b', '--batch-size', type=int, default=500,
                        help='batch_size to use for the minibatch kmeans')
    parser.add_argument('-s', '--save-dir', type=str, required=True,
                        help='save directory for sorted hierarchical kmeans vectors')
    parser.add_argument('-c', '--centroid-dir', type=str, required=True,
                        help='directory to save the centroids in')
    parser.add_argument('-hr', '--hierarchies', type=int, required=True,
                        help='number of hierarchies to run the kmeans on')
    parser.add_argument('-k', '--clusters', type=int, required=True,
                        help='number of clusters for each part of the hierarchy')
    parser.add_argument('-e', '--epochs', type=int, default=15,
                        help='number of epochs to run the kmeans for each hierarchy')
    args = parser.parse_args()

    root = args.root_feature_path
    prefix = args.features_prefix
    batch_size = args.batch_size
    save_dir = args.save_dir
    centroid_dir = args.centroid_dir
    h = args.hierarchies
    k = args.clusters
    epochs = args.epochs

    hkmeans(root, prefix, h, k, batch_size, epochs, save_dir, 'vecs', centroid_dir)


if __name__ == "__main__":
    main()
