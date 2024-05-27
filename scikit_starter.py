import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

wine_data = load_wine()
wine_df = pd.DataFrame(wine_data.data, columns = wine_data.feature_names)
wine_df['target'] = wine_data.target

X = wine_df[wine_data.feature_names].copy()
y = wine_df["target"].copy()

scaler = StandardScaler()
scaler.fit(X)

X_scaled = scaler.transform(X)

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y, train_size = .7, random_state = 25)

logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()

logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

model_preds = {
    'Logistic Regression': log_reg_preds,
    'Support Vector Machine': svm_preds,
    'Decision Tree': tree_preds
}

for model, preds in model_preds.items():
    print(f'{model} Results:\n{classification_report(y_test, preds)}', sep='\n\n')
