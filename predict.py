import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_status(fill, weight, time):

    if fill >= 80:
        return "🚨 ALERT: Garbage Bin is 80% FULL or MORE!"

    result = model.predict([[fill, weight, time]])

    if result[0] == 1:
        return "Bin is FULL 🚨"
    else:
        return "Bin is NOT FULL ✅"