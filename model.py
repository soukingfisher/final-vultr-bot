import pickle

class FinancialAdviceModel:
    def __init__(self, model_path='models/advice_model.pkl'):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def generate_advice(self, data):
        prediction = self.model.predict([[data]])
        return f"Based on your profile, a recommended investment amount is approximately ${prediction[0]:.2f}."
