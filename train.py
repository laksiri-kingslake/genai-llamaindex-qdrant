"""
MLflow training script"""

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the dataset
data = load_diabetes()
X = data.data
y = data.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Set model parameters
alpha = 0.5
l1_ratio = 0.5

# set mlflow tracking uri
mlflow.set_tracking_uri('http://127.0.0.1:3001/')

# Start an MLflow experiment
with mlflow.start_run():
    # Train the model
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    model.fit(X_train, y_train)

    # Predict on the test set
    predictions = model.predict(X_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Log parameters and metrics with MLflow
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    # Log the model itself
    mlflow.sklearn.log_model(model, "model")

    # Advanced Use: Generate a plot for residuals
    plt.scatter(y_test, predictions)
    plt.xlabel("True Values")
    plt.ylabel("Predictions")
    plt.savefig("residuals_plot.png")

    # Log the plot as an artifact
    mlflow.log_artifact("residuals_plot.png")

print("MLflow run complete!")
