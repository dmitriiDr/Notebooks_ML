"""
Created on Tue Sep  3 10:52:32 2024.

@author: dmitrii.druzhbin@Digital-Grenoble.local
"""
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.metrics import silhouette_score
from tools_kmeans import (initialize_centroids,
                          assign_clusters,
                          update_centroids)


class KMeans:
    """My KMEans algo."""

    def __init__(self, k, max_iter=100, pca=False, n_init=10):
        self.k = k
        self.max_iter = max_iter
        self.centroids = None
        self.labels_ = None
        self.pca = pca
        self.n_init = n_init  # initializations

    def fit(self, X, y=None):
        """Fitting function."""
        # Initilize centroids, calculates the dist (Euclid),
        # moves the centroids, calculates the convergencies, repeats.
        # implemented pca so it could be properly plotted (mb not needed)
        best_silhouette = -1
        best_centroids = None
        best_labels = None

        if self.pca:
            pca = PCA(n_components=2)
            X = pd.DataFrame(pca.fit_transform(X))

        self.centroids = initialize_centroids(X, self.k)

        # Run n_init times to find the best initialization
        for _ in range(self.n_init):
            self.centroids = initialize_centroids(X, self.k)
            # iterate until it converges (centroids are stable)
            for i in range(self.max_iter):

                self.labels_ = assign_clusters(X, self.centroids)
                new_centroids = update_centroids(X, self.labels_, self.k)

                if np.all(self.centroids == new_centroids):
                    break

            self.centroids = new_centroids
            silhouette_avg = silhouette_score(X, self.labels_)
            # print(f'silhouette_score: {silhouette_avg:.3f}')

            # Check if this is the best run so far
            if silhouette_avg > best_silhouette:
                best_silhouette = silhouette_avg
                best_centroids = self.centroids
                best_labels = self.labels_
                # print(f'Best: {silhouette_avg:.3f}')
                # print('================================================')

        # Store the best results
        self.centroids = best_centroids
        self.labels_ = best_labels

        return self.labels_, self.centroids

    # functions below is just to try to make it look like KMeans from scikit
    def predict(self, X):
        """Predict the closest cluster each sample in X belongs to."""
        distances = np.sqrt(
            ((X - self.centroids[:, np.newaxis])**2).sum(axis=2))

        return np.argmin(distances, axis=0)

    def score(self, X, y=None):
        """Return the silhouette score depending on the scoring strategy."""
        # self.fit(X)

        return silhouette_score(X, self.labels_)

    def get_params(self, deep=True):
        """Return parameters."""
        return {'k': self.k, 'max_iter': self.max_iter, 'pca': self.pca}

    def set_params(self, **params):
        """Set parameters."""
        for param, value in params.items():
            setattr(self, param, value)
        return self
