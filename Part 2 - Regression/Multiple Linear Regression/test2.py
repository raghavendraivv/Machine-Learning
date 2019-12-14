import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le_x = LabelEncoder()
x[:, 3] = le_x.fit_transform(x[:, 3])
o = OneHotEncoder(categorical_features = [3])
x = o.fit_transform(x).toarray()

"""avoinding duming variables trap"""
x=x[:, 1:]


from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33,random_state= 0)


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train, y_train)

y_pred = reg.predict(x_test)

import statsmodels.formula.api as sm
x = np.append(arr = np.ones([50,1]).astype(int), values = x,axis = 1 )
x_opt = x[:, [0,1,2,3,4,5]]
reg_OLS = sm.OLS(endog = y, exog = x_opt).fit()
print(reg_OLS.summary())
x_opt = x[:, [0,3]]
reg_OLS = sm.OLS(endog = y, exog = x_opt).fit()
print(reg_OLS.summary())

