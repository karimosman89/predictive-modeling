from model import PredictiveModel
import pandas as pd

model = PredictiveModel()
model.load_model('model.pkl')

input_data = pd.DataFrame({
    'feature1': [value1],
    'feature2': [value2],
    # Add other features
})

predictions = model.predict(input_data)
print(predictions)
