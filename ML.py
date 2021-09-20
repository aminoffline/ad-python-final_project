import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.preprocessing import QuantileTransformer, OneHotEncoder, FunctionTransformer , QuantileTransformer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from Database import read_distinct_column

table_name = 'dataset'
table_key = ['model', 'mileage', 'age','color', 'accident', 'owners','price']

data = read_distinct_column(table_name,'model, mileage, age, color, accident, owners,price')
x, y = [], []
data = [i for i in data]

for model, mileage, age, color, accident, owners,price in data:
    x.append([model,mileage,age,color,accident,owners])
    y.append(price)

def get_text(x):
    t_data =[]
    for i in x:
        t_data.append([i[0],i[3]])
    return t_data
def get_numberic(x):
    n_data = []
    for i in x:
        n_data.append([i[1],i[2],i[4],i[5]])
    return n_data

#transfomer_numeric = FunctionTransformer(get_numberic)
#transformer_text = FunctionTransformer(get_text)
"""
Z = QuantileTransformer().fit_transform(get_numberic(x))
x_text = OneHotEncoder(handle_unknown='ignore').fit_transform(get_text(x))
x_text = QuantileTransformer().fit_transform(x_text)
X = list(zip(x_text,Z))
Y =FunctionTransformer(y)
mod = DecisionTreeRegressor()
mod.fit(X,Y)
print(X[1])

"""enc = OneHotEncoder(handle_unknown='ignore')
X = enc.fit_transform(x)
x_data = list(zip(X,z))
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_data, y)
#Ford F-150,135972,5,White,0,2,23997
clf.predict(['Ford F-150',135972,5,'black',0,2])
"""
def get_text(x):
    t_data =[]
    for i in x:
        t_data.append((i[0],i[3]))
    return t_data
def get_numberic(x):
    n_data = []
    for i in x:
        n_data.append((i[1],i[2],i[4],i[5]))
    return n_data

t = ['Ford F-150',135972,5,'black',0,2]

"""
transfomer_numeric = FunctionTransformer(get_numberic)
transformer_text = FunctionTransformer(get_text)

# Create a pipeline to concatenate Tfidf Vector and Numeric data
# Use RandomForestClassifier as an example
pipeline = Pipeline([
    ('features', FeatureUnion([
            ('numeric_features', Pipeline([
                ('selector', transfomer_numeric)
            ])),
             ('text_features', Pipeline([
                ('selector', transformer_text),
                ('vec', TfidfVectorizer(analyzer='word'))
            ]))
         ])),
    ('clf',LinearRegression() )
])

# Grid Search Parameters for RandomForest
param_grid = {'clf__min_samples_split': [3, 10]}
# Training config
kfold = StratifiedKFold(n_splits=7)
scoring = {'Accuracy': 'accuracy', 'F1': 'f1_macro'}
refit = 'F1'

# Perform GridSearch
#rf_model = GridSearchCV(pipeline, param_grid=param_grid, cv=kfold, scoring=scoring,
                         refit=refit, n_jobs=-1, return_train_score=True, verbose=1)
rf_model = GridSearchCV(estimator=pipeline,cv=kfold,
                          n_jobs=-1, return_train_score=True)
rf_model.fit(x, y)
rf_best = rf_model.best_estimator_
rf_model.predict([get_numberic(t),get_text(t)])
"""
t_d = get_text(x)
n_d = get_numberic(x)
ohe = OneHotEncoder(handle_unknown='ignore')
Lin = LinearRegression()
tree = tree.DecisionTreeRegressor()
KN = KNeighborsRegressor()
#le.fit(n_d)
X_data = list(zip(ohe.fit_transform(t_d),n_d))
XXX = list(
    zip(
        ohe.fit_transform(np.array(Model).reshape(-1,1)),ohe.fit_transform(np.array(Color).reshape(-1,1)),np.array(Mileage).reshape(-1,1),np.array(Age).reshape(-1,1),
        np.array(Accident).reshape(-1,1),np.array(Owners).reshape(-1,1)
    )
)
#list(zip(ohe.fit_transform(np.array(Model).reshape(-1,1)),ohe.fit_transform(np.array(Color).reshape(-1,1)),Mileage,Age,Accident,Owners))
p_vals = f_regression(XXX,y)[1]
p_vals = p_vals.round(5)
#mod = KN.fit(X_data,y)


"""
pip = Pipeline(
    [
        ('n_data',QuantileTransformer().fit_transform(get_numberic)),
        ('t_data',OneHotEncoder(handle_unknown='ignore').fit_transform(get_text)),
        ('X',zip(n_data,t_data))
        ('model',DecisionTreeRegressor())
    ]
)
pip.fit(x,y)