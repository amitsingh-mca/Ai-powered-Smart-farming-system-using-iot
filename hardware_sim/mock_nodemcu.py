# hardware_sim/mock_nodemcu.py

import time
import random
import requests

# Flask Server ka local endpoint URL
SERVER_URL = "http://127.0.0.1:5000/api/sensor-data"

print("==================================================")
print("   IoT NODE-MCU HARDWARE SIMULATOR STARTING...   ")
print("==================================================")

try:
    while True:
        # Real-time environment data simulate karne ke liye values
        # Temperature: 25°C se 42°C ke beech
        temperature = round(random.uniform(25.0, 42.0), 1)
        
        # Atmospheric Humidity: 40% se 95% ke beech
        humidity = round(random.uniform(40.0, 95.0), 1)
        
        # Soil Moisture: 10% se 80% ke beech
        moisture = round(random.uniform(10.0, 80.0), 1)
        
        # JSON Payload taiyar karna jo NodeMCU bhi bhejega
        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "moisture": moisture
        }
        
        print(f"\n[IoT Node] Reading Sensors -> Temp: {temperature}°C, Humid: {humidity}%, Soil: {moisture}%")
        
        try:
            # Server ko HTTP POST request bhejna
            response = requests.post(SERVER_URL, json=payload, timeout=5)
            
            if response.status_code == 200:
                result = response.json()
                pump_action = "ON" if result.get("pump_status") == 1 else "OFF"
                print(f"[Server Response] Success! AI Decision: Pump -> {pump_action}")
                print(f"[AI Reason] {result.get('message')}")
            else:
                print(f"[Server Response] Error Code: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("[Error] Unable to connect to Flask Server. Make sure app.py is running on port 5000.")
            
        # Har 4 seconds me data khet se server par bhejenge
        time.sleep(4)

except KeyboardInterrupt:
    print("\n[IoT Node] Simulator stopped by user.")
