import pandas as pd

df=pd.read_csv("win_probability_dataset.csv")

train= df[df['season']<=2022]
test= df[df['season']>=2023]

# print(f"Train rows: {len(train)}")
# print(f"Test rows: {len(test)}")
# print(f"Train seasons: {sorted(train['season'].unique())}")
# print(f"Test seasons: {sorted(test['season'].unique())}")

num_features=['current_score', 'wickets_in_hand', 'balls_remaining', 'runs_needed'
              ,'crr', 'rrr']
cat_features=['batting_team', 'bowling_team']

X_train= train[num_features+cat_features]
Y_train= train['label']

X_test= test[num_features+cat_features]
Y_test=test['label']

# print(X_train.shape)
# print(X_train.head(3))

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


pre = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features),
    ('num', StandardScaler(), num_features)
])

model= Pipeline([
    ('prep',pre),
    ('clif', LogisticRegression(max_iter=1000))
])

# print("Pipline built successfully")

model.fit(X_train, Y_train)
# print("Model trained")

from sklearn.metrics import accuracy_score , log_loss , roc_auc_score

y_pred= model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:,1]

# print(f"Accuracy: {accuracy_score(Y_test, y_pred):.3f}")
# print(f"ROC-AUC: {roc_auc_score(Y_test, y_pred_proba):.3f}")
# print(f"Log loss: {log_loss(Y_test, y_pred_proba):.3f}")

import joblib
joblib.dump(model, "win_prob_model.pkl")
print("Model saved.")