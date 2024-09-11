"""Number of functions required for k-means clustering."""
# function KMeans(D, k, max_iter):
#     # Step 1: Initialize centroids

#     Centroids = Initialize_k_random_centroids(D, k)

#     for i = 1 to max_iter do:

#         # Step 2: Assign each data point to the nearest centroid

#         Clusters = Assign_points_to_nearest_centroid(D, Centroids)


#         # Step 3: Update the centroids based on the new clusters

#         New_Centroids = Calculate_new_centroids(Clusters)


#         # Step 4: Check for convergence

#         if Centroids == New_Centroids ===>:
#             break

#         Centroids = New_Centroids

#     return Clusters, Centroids

# function Initialize_k_random_centroids(D, k):
#     Centroids = select k random unique points from D
#     return Centroids


import numpy as np


def initialize_centroids(X, k):
    """Initialize random centroids, takes data X and number of clusters."""
    n_samples, n_features = X.shape
    centroids = X.to_numpy()[np.random.choice(n_samples, k, replace=False)]
    return centroids


def assign_clusters(X, centroids):
    """Assign the nearest data points to clusters."""
    # Perform broadcasting so that X and centroids have compatible shapes.
    # X has shape (n_samples, n_features) and centroids originally
    # have shape (k, n_features).
    #
    # Distance is calculated using the Euclidean formula, with summation
    # done along n_features.
    # The result has shape (k, n_samples), representing the distance to
    # each centroid for each sample.

    distances = np.sqrt(
        ((X.to_numpy() - centroids[:, np.newaxis])**2).sum(axis=2))

    # Find the centroid with the smallest distance to each data point.
    # Returns a 1D array of cluster labels.

    cluster_labels = np.argmin(distances, axis=0)
    return cluster_labels


def update_centroids(X, cluster_labels, k):
    """Move centroids to new positions."""
    # used average between points in a cluster

    new_centroids = np.array(
        [X.to_numpy()[cluster_labels == i].mean(axis=0) for i in range(k)]
    )
    return new_centroids
