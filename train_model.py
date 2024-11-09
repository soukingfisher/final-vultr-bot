# models/train_model.py
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate synthetic data
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
model = LinearRegression()
model.fit(X, y)

# Save the model
with open('models/advice_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model trained and saved as 'advice_model.pkl'")
