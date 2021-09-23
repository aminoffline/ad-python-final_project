import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import QuantileTransformer, LabelEncoder
from sklearn.pipeline import Pipeline
from Database import read_distinct_column, cursor
import datetime
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
warnings.filterwarnings("ignore")

table_name = 'dataset'
table_key = ['model', 'mileage', 'age','color', 'accident', 'owners','price']
all_models = read_distinct_column(table_name,'model')
all_models = [i[0] for i in all_models]
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

"""
By using Feature selection tools we can detect which feature is useful for our model which not
in our case by using f_regression() and finding p_values for our model 
We came to this conclusion that using 'Color' is not useful for our model
so we dropped it .  
"""

la = LabelEncoder()
x = list(zip(la.fit_transform(Model),Mileage,Age,Accident,Owners))
pipe = Pipeline([
    ("scale",QuantileTransformer()),
    ("model",DecisionTreeRegressor())
])
mod = GridSearchCV(estimator=pipe,param_grid={'model__min_samples_leaf': [1,2,3,4], 'model__min_samples_split': [2,3,4,5],'scale__n_quantiles': [25,500,1000,2000,4000]},n_jobs=-1, cv=10)
MOD = mod.fit(x, y)

def price_predict(model, mileage, year_model, accident, owners):
    model = model.casefold()
    today = datetime.date.today()
    age = today.year - int(year_model)
    if model in all_models:
        pre_in = [(la.fit_transform([model]), mileage, age, accident, owners)]
        price = MOD.predict(pre_in)
        return print(f'predicted price of {model}: {int(price)} $')
    else:
        return print(f'Input Model is not in our Trained Database; Please check Model name or look at Model Database Below \n \n {all_models} ')


price_predict(input('model: '),float(input('Mileage: ')),int(input('Year model: ')),int(input('Number of Accidents: ')),int(input('Number of Owners: ')))

#price_predict('nissan altima',100000000,2015,0,1)