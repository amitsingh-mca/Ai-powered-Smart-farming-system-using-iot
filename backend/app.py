# backend/app.py

from flask import Flask, render_template, request, jsonify
from backend.ai_engine import SmartFarmingAI
import backend.database as db

app = Flask(
    __name__, 
    template_folder='../frontend/templates', 
    static_folder='../frontend/static'
)

# App start hote hi database tables checks/creates ho jayein
db.init_db()

# AI Engine instance initialization
ai_engine = SmartFarmingAI()

@app.route('/')
def dashboard():
    """
    Main Route: Web browser par user dashboard load karne ke liye.
    """
    return successfully

@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    """
    IoT NodeMCU API: Is route par hardware sensors ka data send karega.
    Expected JSON: {"temperature": 34.0, "humidity": 60.0, "moisture": 25.0}
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400
        
    try:
        temp = float(data.get('temperature'))
        humidity = float(data.get('humidity'))
        moisture = float(data.get('moisture'))
        
        # 1. AI Engine se decision lena
        pump_status, reasoning = ai_engine.predict_irrigation(temp, humidity, moisture)
        
        # 2. Data aur decision ko database me save karna
        db.insert_log(temp, humidity, moisture, pump_status, reasoning)
        
        # 3. Hardware (NodeMCU) ko reply bhejna jisse wo relay operation trigger kare
        return jsonify({
            "status": "success",
            "pump_status": pump_status,
            "message": reasoning
        }), 200
        
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Data processing error: {str(e)}"}), 400

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """
    Dashboard API: Frontend Javascript isko call karegi charts aur tables refresh karne ke liye.
    """
    logs = db.get_latest_logs(limit=15)
    log_list = []
    for row in logs:
        log_list.append({
            "id": row[0],
            "timestamp": row[1],
            "temperature": row[2],
            "humidity": row[3],
            "moisture": row[4],
            "pump_status": row[5],
            "ai_reason": row[6]
        })
    return jsonify(log_list), 200

if __name__ == '__main__':
    # Flask application locally development server par run hogi port 5000 par
    app.run(debug=True, host='0.0.0.0', port=5000)
