import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load data
data = pd.read_csv("Student_Performance.csv")

# Drop unwanted columns
data = data.drop(columns=["student_id", "final_grade"])

# One-hot encode categorical columns
data = pd.get_dummies(data, drop_first=True)

# Split features & target
X = data.drop(columns=["overall_score"])
y = data["overall_score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate (important for interview)
pred = model.predict(X_test)
mse = mean_squared_error(y_test, pred)
print("MSE:", mse)

# Save model + columns
joblib.dump((model, X.columns), "model.pkl")

print("Model trained successfully ✅")