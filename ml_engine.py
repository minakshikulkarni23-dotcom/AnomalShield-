import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

class TransactionGuard:
    def __init__(self, model_path="iforest_model.joblib"):
        self.model_path = model_path
        self.model = IsolationForest(contamination=0.01, random_state=42)

    def train_and_save(self):
        # Directly create a small matrix to prevent freezing
        X = np.array([
            [50.0, 14, 2, 3],
            [20.0, 12, 1, 1],
            [10.0, 9, 3, 2],
            [100.0, 16, 2, 4],
            [35.0, 15, 1, 2]
        ])
        # Repeat the pattern to fit the model quickly
        data = np.repeat(X, 20, axis=0)
        
        self.model.fit(data)
        joblib.dump(self.model, self.model_path)
        print("Model successfully saved to iforest_model.joblib")

    def evaluate_transaction(self, features):
        try:
            model = joblib.load(self.model_path)
        except FileNotFoundError:
            raise RuntimeError("Model file not found.")
        prediction = model.predict(np.array(features).reshape(1, -1))
        return int(prediction[0])

if __name__ == "__main__":
    guard = TransactionGuard()
    guard.train_and_save()