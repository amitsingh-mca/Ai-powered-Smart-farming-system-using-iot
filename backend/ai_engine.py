# backend/ai_engine.py

class SmartFarmingAI:
    def __init__(self):
        # Yahan hum threshold values define kar rahe hain
        # Inhe future me real-time ML model training se optimize kiya ja sakta hai
        self.moisture_threshold_dry = 30.0  # Percentage
        self.humidity_threshold_rain = 85.0 # Percentage
        self.temp_critical_hot = 38.0       # Celsius

    def predict_irrigation(self, temperature, humidity, moisture):
        """
        AI Framework: Multi-variable decision making engine.
        Returns: Tuple (action_code, reasoning_message)
        action_code: 1 for Pump ON, 0 for Pump OFF
        """
        
        # Scenario 1: Mitti bhot sukhi hai aur tapman bhot zyada hai (Critical Alert)
        if moisture < self.moisture_threshold_dry and temperature >= self.temp_critical_hot:
            return 1, "CRITICAL: Extreme heat and dry soil detected. Immediate watering required."
            
        # Scenario 2: Mitti sukhi hai, lekin hawa me humidity bhot high hai (Rain Prediction)
        elif moisture < self.moisture_threshold_dry and humidity >= self.humidity_threshold_rain:
            return 0, "STANDBY: Soil is dry, but high atmospheric humidity indicates imminent rain. Delaying irrigation to conserve water."
            
        # Scenario 3: Mitti normal sukhi hai aur mausam bhi normal hai
        elif moisture < self.moisture_threshold_dry:
            return 1, "OPTIMAL: Soil moisture dropped below threshold. Turning pump ON."
            
        # Scenario 4: Mitti me proper nami hai
        else:
            return 0, "SAFE: Soil moisture is adequate. Pump remains OFF."

# Self-testing block (Sirf check karne ke liye ki engine sahi kaam kar raha hai ya nahi)
if __name__ == "__main__":
    ai = SmartFarmingAI()
    # Test case: Dry soil but heavy cloud/humidity
    code, msg = ai.predict_irrigation(temperature=32.0, humidity=90.0, moisture=20.0)
    print(f"Test Result -> Code: {code} | Message: {msg}")
