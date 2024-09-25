from model import PredictiveModel
from utils import load_and_split_data

X_train, X_test, y_train, y_test = load_and_split_data('data/dataset.csv', 'target')

model = PredictiveModel()
model.train(X_train, y_train)
model.save_model('model.pkl')

print(f'Model evaluation: {model.evaluate(X_test, y_test)}')
