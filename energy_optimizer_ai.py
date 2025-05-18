
import random
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import joblib
from cryptography.fernet import Fernet
import time

class EnergyOptimizerAI:
    def __init__(self):  # Fixed constructor
        self.model = GradientBoostingRegressor()

    def train_model(self, data):
        X = data[['temperature', 'occupancy', 'hour']]
        y = data['energy_usage']
        self.model.fit(X, y)
        joblib.dump(self.model, 'ai_energy_model.pkl')

    def predict_energy(self, input_features):
        # Directly use the trained model
        return self.model.predict([input_features])[0]

def simulate_iot_sensor():
    return {
        'temperature': random.uniform(17, 34),
        'occupancy': random.randint(0, 20),
        'hour': random.randint(0, 23),
        'energy_usage': random.uniform(150, 2700)
    }

def create_dataset(size=250):
    return pd.DataFrame([simulate_iot_sensor() for _ in range(size)])

def encrypt_data(data, key):
    return Fernet(key).encrypt(data.encode())

def decrypt_data(encrypted, key):
    return Fernet(key).decrypt(encrypted).decode()

def chatbot(query):
    q = query.lower()
    if "optimize" in q:
        return "Reduce HVAC 2-4 PM, use motion lights."
    elif "usage" in q:
        return "Avg usage: 1125W. Try smart scheduling."
    elif "save" in q:
        return "Use efficient devices, run off-peak."
    else:
        return "Ask about energy saving or usage tips."

def test_performance(model, sample_input):
    start = time.time()
    for _ in range(100):
        model.predict_energy(sample_input)
    return round(time.time() - start, 3)

def main():
    print("AI-Energy Efficiency Optimization System Demonstration")
    print("------------------------------------------------------")
    data = create_dataset()
    ai_model = EnergyOptimizerAI()
    ai_model.train_model(data)
    print("Model trained with real-time IoT data.")

    test_input = [24.5, 6, 13]
    prediction = ai_model.predict_energy(test_input)
    print(f"Predicted Energy Usage: {prediction:.2f}W")

    response1 = chatbot("how do I optimize energy?")
    print(f"Chatbot: {response1}")

    response2 = chatbot("current energy usage")
    print(f"Chatbot: {response2}")

    key = Fernet.generate_key()
    encrypted = encrypt_data("Confidential Usage Data: 1180w", key)
    decrypted = decrypt_data(encrypted, key)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

    latency = test_performance(ai_model, [21.0, 3, 18])
    print(f"System Response Time under Load: {latency} seconds")

main()
