import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

df = pd.read_excel(f'D:/DSFiles/bk/data/all.xlsx',
                   names=['place', 'title', 'msg', 'price', 'per_meter',
                          'year', 'area', 'age', 'lat', 'lng', 'income', 'loc'])

df.drop(df[(df['age'].isnull())].index, inplace=True)
df.drop(df[(df['per_meter'].isnull())].index, inplace=True)
lines = df.shape[0]

#  赋值
X = df.loc[:, ['area', 'age', 'income', 'loc']]
y = df.loc[:, 'price']
X = np.array(X)
y = np.array(y)
X = X.reshape(-1, 4)
y = y.reshape(-1, 1)

model = LinearRegression()
model.fit(X, y)
cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')
y_predict = model.predict(X)

MSE = mean_squared_error(y, y_predict)
R2 = r2_score(y, y_predict)

print('Mse: ', round(MSE, 2))
print('R2: ', round(R2, 2))

fig = plt.figure(figsize=(8, 5))
plt.scatter(y, y_predict, s=15)
plt.plot(y, y, 'r')
plt.title('House-price LinearRegression')
plt.xlabel('real price')
plt.ylabel('predicted price')

plt.show()





''''''

'''
fig = plt.figure(figsize=(10, 10))
fig1 = plt.subplot(221)
plt.scatter(df.loc[:, 'area'], df.loc[:, 'price'])
plt.title('Price & Size')
fig2 = plt.subplot(222)
plt.scatter(df.loc[:, 'age'], df.loc[:, 'price'])
plt.title('Price & Size')
fig3 = plt.subplot(223)
plt.scatter(df.loc[:, 'income'], df.loc[:, 'price'])
plt.title('Price & Size')
fig4 = plt.subplot(224)
plt.scatter(df.loc[:, 'loc'], df.loc[:, 'price'])
plt.title('Price & Size')
plt.show()
'''
