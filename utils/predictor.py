import pandas as pd

def predict_price(model, data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return prediction[0]