import pandas as pd

df=pd.read_csv("win_probability_dataset.csv")

train= df[df['season']<=2022]
test= df[df['season']>=2023]

print(f"Train rows: {len(train)}")
print(f"Test rows: {len(test)}")
print(f"Train seasons: {sorted(train['season'].unique())}")
print(f"Test seasons: {sorted(test['season'].unique())}")

num_features=['current_score', 'wickets_in_hand', 'balls_remaining', 'runs_needed'
              ,'crr', 'rrr']
cat_features=['batting_team', 'bowling_team']

X_train= train[num_features+cat_features]
Y_train= train['label']

X_test= test[num_features+cat_features]
Y_test=test['label']

print(X_train.shape)
print(X_train.head(3))

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


pre = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
], remainder='passthrough')

model= Pipeline([
    ('prep',pre),
    ('clif', LogisticRegression(max_iter=1000))
])

print("Pipline built successfully")