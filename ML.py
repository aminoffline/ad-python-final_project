import numpy as np
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import QuantileTransformer, LabelEncoder ,RobustScaler ,StandardScaler
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from Database import read_distinct_column
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

table_name = 'dataset'
table_key = ['model', 'mileage', 'age','color', 'accident', 'owners','price']

data = read_distinct_column(table_name,'model, mileage, age, color, accident, owners,price')
x, y = [], []
Model,Color,Mileage,Age,Accident,Owners = [],[],[],[],[],[]
data = [i for i in data]

for model, mileage, age, color, accident, owners,price in data:
    x.append([model,mileage,age,color,accident,owners])
    Model.append(model)
    Color.append(color)
    Mileage.append(mileage)
    Age.append(age)
    Accident.append(accident)
    Owners.append(owners)
    y.append(price)

t = ['Ford F-150',135972,5,'black',0,2]
#t = ['Ford F-150',135972,1,'black',0,1]
#Ford F-150,150196,3,White,0,1,25000
t = ['Ford F-150',150196,3,'black',0,1]

la = LabelEncoder()
x = list(zip(la.fit_transform(Model),Mileage,Age,Accident,Owners))
pipe = Pipeline([
    ("scale",QuantileTransformer()),
    ("model",DecisionTreeRegressor())
])
mod = GridSearchCV(estimator=pipe,param_grid={'model__min_samples_leaf': [1,2,3,4], 'model__min_samples_split': [2,3,4,5],'scale__n_quantiles': [25,500,1000,2000,4000]},n_jobs=-1, cv=10)

pre_in = [(la.fit_transform([t[0]]),t[1],t[2],t[4],t[5])]
MOD = mod.fit(x,y)
re= MOD.predict(x)

plt.scatter(y-re,y,color='green')
plt.savefig('re.png')


