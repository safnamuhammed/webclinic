# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 03:30:45 2026

@author: SCMS
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


# 2. Load the dataset
df = pd.read_csv("carage.csv")


# 3. Explore the dataset
print("First 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())


# 4. Check for missing values
print("\nMissing values:")
print(df.isnull().sum())


# If missing values exist, remove them
df = df.dropna()


# 5. Identify independent and dependent variables
# Independent variable (X): Car_Age
# Dependent variable (y): Resale_Price

X = df[["Car_Age"]]
y = df["Resale_Price"]


# 6. Split the dataset into training and testing sets
# 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)


# 7. Build and train the Linear Regression model
model = LinearRegression()

model.fit(X_train, y_train)


# 8. Predict resale prices for the test data
y_pred = model.predict(X_test)

print("\nPredicted resale prices:")
print(y_pred)


# 9. Display regression coefficient and intercept
print("\nRegression Coefficient (Slope):")
print(model.coef_[0])

print("\nIntercept:")
print(model.intercept_)


# 10. Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R²   :", r2)


# 11. Plot actual data points and fitted regression line
plt.figure(figsize=(8, 5))

# Actual data points
plt.scatter(
    X, y,
    color="blue",
    label="Actual Data"
)

# Regression line
plt.plot(
    X,
    model.predict(X),
    color="red",
    linewidth=2,
    label="Regression Line"
)

plt.xlabel("Car Age (Years)")
plt.ylabel("Resale Price")
plt.title("Car Age vs Resale Price - Linear Regression")
plt.legend()
plt.grid(True)

plt.show()


# 12. Predict resale price of a 5-year-old car
car_age_5 = pd.DataFrame({"Car_Age": [5]})

predicted_price = model.predict(car_age_5)

print("\nPredicted resale price for a 5-year-old car:")
print(predicted_price[0])