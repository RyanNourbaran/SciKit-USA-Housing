#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns # for visualization
%matplotlib inline

df = pd.read_csv('./USA_Housing.csv')

#scikit
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#errors
from sklearn import metrics

#read dataset using pandas
dataframe = pd.read_csv('./USA_Housing.csv')

#save all columns except price (isolated), and address (useless)
indepvars = dataframe.drop(['Price', 'Address'], axis=1)
print(indepvars.columns)
#isolate price or comparison
p = dataframe['Price']
#split dataset into a training set (30%) and a testing set (70%)
indepvars_train, indepvars_test, p_train, p_test = train_test_split(
    indepvars, p, test_size=0.3, random_state=42)

#start a linear regression model
lm = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

#fit model to our independant variables and the price training sets
lm.fit(indepvars_train, p_train)


# (lm.coef_) now contains the coefficients of each column.
#  Values are the increase in price per unit increase of coefficient

# set each coefficient to a column name in a dataframe
coeff = pd.DataFrame(lm.coef_, indepvars.columns, columns=['coefficients'])

#print(coeff)

#now use the linear model we trained to test on the remaining independent variables
predictions = lm.predict(indepvars_test)

#@@@@@@@@@@@@@@@@@@@@@79545.458574,5.682861,7.009188,2, 100000   

#plot the actual test values versus our prediction
# residuals (difference between the p_test points and prediction points) are the error
#sns.jointplot(p_test, predictions)

print('Mean Absolute Error',metrics.mean_absolute_error(p_test, predictions))
print('Mean Squared Error',metrics.mean_squared_error(p_test, predictions))
print('Root Mean Squared Error',np.sqrt(metrics.mean_squared_error(p_test, predictions)))
