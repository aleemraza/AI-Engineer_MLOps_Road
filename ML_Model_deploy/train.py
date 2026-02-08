import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dataset
X, y = load_iris(return_X_y=True)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")
