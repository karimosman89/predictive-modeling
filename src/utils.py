import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data(data_path, target_column):
    data = pd.read_csv(data_path)
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)
