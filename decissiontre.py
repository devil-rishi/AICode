import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def gini_impurity(y):
    counts = np.bincount(y)
    probabilities = counts / len(y)
    return 1 - np.sum(probabilities**2)

def split_dataset(X, y, feature, threshold):
    left_indices = np.where(X[:, feature] <= threshold)[0]
    right_indices = np.where(X[:, feature] > threshold)[0]
    return left_indices, right_indices

def best_split(X, y):
    num_samples, num_features = X.shape
    best_gini = float('inf')
    best_feature, best_threshold = None, None
    
    for feature in range(num_features):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_indices, right_indices = split_dataset(X, y, feature, threshold)
            if len(left_indices) == 0 or len(right_indices) == 0:
                continue
            left_gini = gini_impurity(y[left_indices])
            right_gini = gini_impurity(y[right_indices])
            weighted_gini = (len(left_indices)/num_samples) * left_gini + (len(right_indices)/num_samples) * right_gini
            
            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_feature = feature
                best_threshold = threshold
                
    return best_feature, best_threshold

def most_common_label(y):
    counter = Counter(y)
    most_common = counter.most_common(1)[0][0]
    return most_common

def build_tree(X, y, depth=0, max_depth=3, min_samples_split=2):
    num_samples, num_features = X.shape
    num_labels = len(set(y))
    
    # stopping conditions
    if (depth >= max_depth or num_labels == 1 or num_samples < min_samples_split):
        return most_common_label(y)
    
    feature, threshold = best_split(X, y)
    if feature is None:
        return most_common_label(y)
    
    left_indices, right_indices = split_dataset(X, y, feature, threshold)
    
    left_subtree = build_tree(X[left_indices], y[left_indices], depth+1, max_depth, min_samples_split)
    right_subtree = build_tree(X[right_indices], y[right_indices], depth+1, max_depth, min_samples_split)
    
    return (feature, threshold, left_subtree, right_subtree)

def predict_sample(tree, x):
    # If leaf node, tree is a label (not a tuple)
    if not isinstance(tree, tuple):
        return tree
    
    feature, threshold, left_subtree, right_subtree = tree
    if x[feature] <= threshold:
        return predict_sample(left_subtree, x)
    else:
        return predict_sample(right_subtree, x)

def predict(tree, X):
    return np.array([predict_sample(tree, x) for x in X])

# Load data
data = load_iris()
X, y = data.data, data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build decision tree
tree = build_tree(X_train, y_train, max_depth=3)

# Predict on test set
predictions = predict(tree, X_test)

# Calculate accuracy
accuracy = np.mean(predictions == y_test)

print("Accuracy:", accuracy)
print("Predictions:", predictions)
print("Actual Labels:", y_test)
