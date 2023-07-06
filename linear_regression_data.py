import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/linear_data.csv')

plt.scatter(data=df, x='X', y='Y')
#plt.show()

#print(df.tail(10))


"""
axis = 0 phep tinh theo chieu doc (theo cac hang)
axis = 1 phep tinh theo chieu ngang (theo cac cot)
"""
df = df.drop(labels=[298,299], axis=0)

X = df['X'].to_numpy().reshape(-1,1)
Y = df['Y'].to_numpy().reshape(-1,1)

#print(X)
#print(Y)


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.33)


