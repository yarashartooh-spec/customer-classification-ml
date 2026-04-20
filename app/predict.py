import pickle
import numpy as np
import os


# Get current file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build paths
model_path = os.path.join(BASE_DIR, "..", "model", "model.pkl")
encoder_path = os.path.join(BASE_DIR, "..", "model", "encoder.pkl")

# Load
model = pickle.load(open(model_path, "rb"))
encoder = pickle.load(open(encoder_path, "rb"))

def predict_customer(total_orders, total_spent, avg_order_value, country):
    """
    Predict if a customer is high-value or low-value
    """

    # Encode country
    try:
        country_encoded = encoder.transform([country])[0]
    except:
        return "Error: Unknown country"

    # Create input
    X = np.array([[total_orders, total_spent, avg_order_value, country_encoded]])

    # Predict
    prediction = model.predict(X)[0]

    return "High Value" if prediction == 1 else "Low Value"


# Example usage
if __name__ == "__main__":
    print("=== Customer Value Prediction ===")

    try:
        total_orders = int(input("Enter total orders: "))
        total_spent = float(input("Enter total spent: "))
        avg_order_value = float(input("Enter average order value: "))
        country = input("Enter country: ")

        result = predict_customer(total_orders, total_spent, avg_order_value, country)

        print("\nPrediction:", result)

    except Exception as e:
        print("Error:", e)