import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, neighbors


iris = datasets.load_iris()

iris_X = iris.data
iris_y = iris.target

num_data = len(iris_X)
print('numbers of data points: %d' %num_data)

l = len(np.unique(iris_y))
print('numbers of classes: %d' %l)

X0 = iris_X[iris_y==0, :]
X1 = iris_X[iris_y==1, :]
X2 = iris_X[iris_y==2, :]


#print('\nSample from class 0: \n',X0[:5, :])
#print('\nSample from class 1: \n',X1[:5, :])
#print('\nSample from class 2: \n',X2[:5, :])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=50)

clf = neighbors.KNeighborsClassifier(n_neighbors=10, p=2, weights='distance')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(y_pred)
print(y_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred)*100)