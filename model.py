import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# import pickle

data = pd.read_csv('iris.csv')
x = data.drop(columns=['species'])
y = data.filter(['species'])
scaler = MinMaxScaler()
data_column_names = x.columns.values
x_scaled = scaler.fit_transform(x)
X=pd.DataFrame(x_scaled, columns=data_column_names)
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size = 0.3)
DTC = DecisionTreeClassifier()

def predictor(sepal_length, sepal_width, petal_length, petal_width):
    DTC.fit(x_train,y_train)
    y_predict = DTC.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return y_predict
