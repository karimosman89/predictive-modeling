import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class PredictiveModel:
    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def save_model(self, filename):
        joblib.dump(self.model, filename)

    def load_model(self, filename):
        self.model = joblib.load(filename)

    def evaluate(self, X_test, y_test):
        predictions = self.predict(X_test)
        return mean_squared_error(y_test, predictions)
