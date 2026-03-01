# Written by: Christopher Gholmieh
# Imports:

# Pandas:
import pandas as pd

# Toolkit:
# > Selection:
from sklearn.model_selection import train_test_split

# > Ensemble:
from sklearn.ensemble import RandomForestRegressor

# > Default:
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Numpy:
import numpy as np


# Variables (Assignment):
# Dataframe:
dataframe = pd.read_csv("expenses_data.csv")

# X:
X = dataframe[["race_is_black", "is_college", "is_hs", "is_lt_15000", "bt_15k_30k", "bt_30k_39k", "bt_40k_49k", "bt_50k_69k", "bt_70k_99k", "bt_100k_149k", "bt_150k_199k"]]

# Y:
y = dataframe["expense"]


# Split:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model:
model = RandomForestRegressor(n_estimators=200)

# Fit:
model.fit(X_train, y_train)

# Prediction:
y_prediction = model.predict(X_test)

# Variables (Assignment):
# Errors:
mean_absolute_err = mean_absolute_error(y_test, y_prediction)
mean_square_err = mean_squared_error(y_test, y_prediction)
root_square_err = np.sqrt(mean_square_err)

# Coefficient:
coefficient = r2_score(y_test, y_prediction)

# Output:
print(f"[*] Predictions on test set: {y_prediction}")
print(f"[+] Mean absolute error: {mean_absolute_err}")
print(f"[+] Mean square error: {mean_square_err}")
print(f"[+] Root square error: {root_square_err}")