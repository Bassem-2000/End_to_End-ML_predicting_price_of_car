
import warnings
warnings.simplefilter(action= 'ignore', category=FutureWarning)
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv('1.04. Real-life example.csv')

data = data.drop(['Model'], axis = 1)


remove_out = data['Price'].quantile(0.97)
data = data[data['Price']<remove_out]
remove_out = data['Mileage'].quantile(0.99)
data = data[data['Mileage']<remove_out]


data = data[data['EngineV']<6.5]


remove_out  = data['Year'].quantile(0.02)
data = data[data['Year']>remove_out]

data['Price'] = np.log(data['Price'])

variables = data[['Mileage','Year','EngineV']]
vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(variables.values, i) for i in range(3)]
vif['Features'] = variables.columns

variables = data[['Mileage','Year']]
vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(variables.values, i) for i in range(2)]
vif['Features'] = variables.columns

data = data.drop('EngineV', axis =1)


data = pd.get_dummies(data)

x = data.drop(['Price'], axis = 1)
y = data['Price']
x.columns.values


y = np.asarray(y).reshape(-1, 1)
y.shape

scaling = StandardScaler()
scaling.fit(x)
x = scaling.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=365)

model = LinearRegression()
model.fit(x_train, y_train)

def user_end(year, mileage, brand, body, engine_type, registration):
    data_copy = pd.DataFrame(columns=data.columns)
    data_copy.loc[0]=0
    data_copy.loc[0, 'Year'] = year
    data_copy.loc[0, 'Mileage'] = mileage
    data_copy.loc[0, brand] = 1
    data_copy.loc[0, body] = 1
    data_copy.loc[0, engine_type] = 1
    data_copy.loc[0, 'Registration_yes'] = registration
    data_copy = data_copy.drop(['Price'], axis = 1)
    c = scaling.transform(data_copy)
    return np.exp(model.predict(c))
#
