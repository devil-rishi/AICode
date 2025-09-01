import numpy as np

from sklearn import datasets
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder


def calculate_class_priors(y):
    classes, counts = np.unique(y, return_counts=True)
    total_samples = len(y)
    class_priors = {c: count/total_samples  for c, count in zip(classes, counts)}
    return class_priors

def calculate_gaussian_parameters(X,y):
    params = {}
    classes = np.unique(y)
    for c in classes:
        X_class =X[y==c]
        params[c] = [(np.mean(X_class[:,i]), np.var(X_class[:,i])) for i in range(X.shape[1])]
    return params

def gaussian_pdf(x,mean,var):
    eps = 1e-6
    coeff =  1.0 / np.sqrt(2.0 * np.pi * var + eps)
    exponent = np.exp(-((x-mean) ** 2) / (2 * var + eps))
    return coeff * exponent

def predict(X, class_priors, params, classes):
    y_pred = []
    for x in X:
        posteriors = {}
        for c in classes:
            posteriors[c] = np.log(class_priors[c])
            for i in range(len(x)):
                mean, var = params[c][i]
                posteriors[c] += np.log(gaussian_pdf(x[i], mean, var))
        y_pred.append(max(posteriors, key=posteriors.get))
    return np.array(y_pred)

def native_bayes_classifire(X_train, y_train, X_test):
    class_priors = calculate_class_priors(y_train)
    params = calculate_gaussian_parameters(X_train, y_train)
    classes = np.unique(y_train)

    y_pred = predict(X_test, class_priors, params, classes)
    return y_pred

iris = datasets.load_iris()
X = iris.data
y = iris.target

kf = StratifiedKFold(n_splits=5, shuffle=True,random_state=42)
accuracies = []

for train_index, test_index in kf.split(X,y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    y_pred = native_bayes_classifire(X_train, y_train, X_test)

    accuracy = np.sum(y_pred == y_test)/ len(y_test)
    accuracies.append(accuracy)

    print(f"Cross-Validation Accuracies: {accuracies}")
    print(f"Mean Accuracy: {np.mean(accuracies)}")
