import unittest
import pandas as pd
from model import PredictiveModel
from utils import load_and_split_data

class TestPredictiveModel(unittest.TestCase):
    def setUp(self):
        self.model = PredictiveModel()
        self.X_train, self.X_test, self.y_train, self.y_test = load_and_split_data('data/dataset.csv', 'target')
        self.model.train(self.X_train, self.y_train)

    def test_prediction(self):
        predictions = self.model.predict(self.X_test)
        self.assertEqual(len(predictions), len(self.y_test))

if __name__ == '__main__':
    unittest.main()
