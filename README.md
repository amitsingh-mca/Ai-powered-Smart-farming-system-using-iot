# Ai-powered-Smart-farming-system-using-iot
An AI-powered autonomous farming framework integrating multivariable data layers—soil moisture, temperature, and humidity—with an asynchronous local SQLite database.
# AI-Powered Smart Farming System using IoT 🌾🤖

An autonomous, production-grade closed-loop automation framework that monitors soil and weather dynamics in real-time. The system leverages a multivariable AI decision engine to optimize crop irrigation, prevent water wastage, and mitigate agricultural heatwave emergencies.

---

## 🛠️ System Architecture

The project is structured as a decentralized IoT network communicating with a local centralized Python Flask server backed by an asynchronous SQLite database layer.



1. **Hardware Node (Edge Layer):** NodeMCU (ESP8266) reads real-time environmental metrics via DHT11 and Soil Moisture sensors.
2. **AI Backend Server (Control Layer):** A Python Flask REST API processes incoming telemetry, runs multivariable predictive rules, and logs results into SQLite.
3. **Digital Twin Dashboard (Presentation Layer):** A premium, minimalistic cyber-tech dashboard showcasing live grid topology mapping and dynamic micro-reservoir simulation tracking.

---

## 📂 Project Structure

```text
SmartFarmingAI/
│
├── backend/                  # Server Framework & Core Decision Layer
│   ├── app.py                # Main Flask Server (REST API Entry Point)
│   ├── ai_engine.py          # Multivariable AI Predictive Model Logic
│   └── database.py           # SQLite Connections & Async Log Registers
│
├── frontend/                 # Presentation View Components
│   ├── static/               # System Asset Bundles (CSS/JS separated)
│   └── templates/            # Single-Page Application (SPA) HTML Shells
│
├── database/                 # Structured Storage Engine
│   └── farming.db            # Auto-generated encrypted SQLite File
│
├── hardware_sim/             # Edge Emulator Module
│   └── mock_nodemcu.py       # Loop script simulating hardware telemetry
│
└── requirements.txt          # Explicit Dependency Map
