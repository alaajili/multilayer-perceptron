import numpy as np


def split_data(X, y, test_size=0.2, random_status=42):
    np.random.seed(random_status)
    n = X.shape[0]
    num_test = int(test_size * n)

    indices = np.arange(n)
    np.random.shuffle(indices)
    train_indices = indices[num_test:]
    test_indices = indices[:num_test]
    X_train = X[train_indices]
    y_train = y[train_indices]
    X_test = X[test_indices]
    y_test = y[test_indices]
    return X_train, y_train, X_test, y_test

        

def min_max_scale(X):
    for i in range(X.shape[1]):
        feature_mean = np.nanmean(X[:, i])
        X[np.isnan(X[:, i]), i] = feature_mean

    min_val = X.min(axis=0)
    max_val = X.max(axis=0)
    X = (X - min_val) / (max_val - min_val)

    return X
        