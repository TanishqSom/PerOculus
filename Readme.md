# 🚀 PerOculus – AI-Powered Disaster Response Drone  
### Hackofiesta 6.0 | IIIT Lucknow | Team Permutes  

**PerOculus** is an AI-driven UAV system designed for **disaster response, search & rescue, and public safety.**  
Using **AI, Computer Vision, and real-time UAV telemetry**, PerOculus can:  
✅ **Predict disasters** using satellite/weather data  
✅ **Detect stranded people & high-risk areas** using AI  
✅ **Deploy autonomously in emergencies**  

---

## 📌 Project Flow – How It Works  
PerOculus follows a **4-stage pipeline** to ensure fast and effective disaster response:  

### **1️⃣ Prediction Layer → AI-Based Risk Assessment**  
- Analyzes **satellite imagery, IMD weather data, and GIS data**  
- Predicts **flood risks, drought-prone areas, and disaster likelihood**  
- Stores **AI-predicted high-risk locations** for UAV deployment  

### **2️⃣ Action Layer → Autonomous UAV Deployment**  
- **ArduPilot-based navigation** with GPS waypoints  
- Executes flight **missions based on Prediction Layer outputs**  
- **Real-time flight telemetry & waypoint adjustments**  

### **3️⃣ Anomaly Detection → AI Object Recognition**  
- Uses **YOLOv8 + OpenCV** to **detect people, debris, vehicles, flood damage**  
- Processes **live FPV drone feed** and marks high-risk zones  
- Outputs **detection logs & alerts to Mission Control**  

### **4️⃣ Mission Control → Live Monitoring & Decision-Making**  
- Web-based **Flask dashboard** with **real-time UAV telemetry**  
- AI-based risk alerts from **Prediction & Anomaly Detection Layers**  
- Sends **rescue team alerts based on drone findings**  

---

## 📂 Repository Structure – Purpose of Each Folder  
```bash
PerOculus/
│── /Prediction_Layer/       # AI-based disaster prediction
│   ├── Data/                # Satellite, GIS, weather data
│   ├── Scripts/             # AI-based flood & risk analysis
│   ├── Output/              # Risk maps & AI-processed data
│   ├── weather_prediction.py # Python risk prediction
│   ├── weather_prediction.cpp # C++ risk prediction
│
│── /Action_Layer/           # UAV Flight Control & Deployment
│   ├── Firmware/            # ArduPilot config files
│   ├── Flight_Logs/         # Logs of test flights
│   ├── Hardware/            # Circuit diagrams, SpeedyBee manual
│   ├── drone_control.py     # Python MAVLink UAV control
│   ├── drone_control.cpp    # C++ MAVSDK UAV control
│
│── /Anomaly_Detection/      # AI Object Detection from UAV
│   ├── Computer_Vision/     # YOLO model weights
│   ├── Analog_Drone_Feed/   # FPV video processing
│   ├── Detection_Logs/      # AI-processed images
│   ├── object_detection.py  # Python AI object detection
│   ├── object_detection.cpp # C++ OpenCV-based detection
│
│── /Mission_Control/        # Ground station & monitoring
│   ├── Waypoints/           # GPS Mission Planner waypoints
│   ├── Dashboard/           # Flask web dashboard
│   ├── Mission_Logs/        # UAV telemetry & AI alerts
│   ├── app.py               # Live telemetry dashboard
│   ├── telemetry.cpp        # C++ telemetry monitoring
│
│── /ROS_Files/              # Future ROS-based automation
│   ├── Placeholder/
│
│── README.md                # Project documentation

```



🚀 Running the System
🔹 1. Start the AI Disaster Prediction (Prediction Layer)
bash
Copy
Edit
python Prediction_Layer/weather_prediction.py
Or C++ version:

bash
Copy
Edit
g++ -o weather_prediction Prediction_Layer/weather_prediction.cpp
./weather_prediction
🔹 2. Start the Drone Flight Control (Action Layer)
bash
Copy
Edit
python Action_Layer/drone_control.py
Or:

bash
Copy
Edit
g++ -o drone_control Action_Layer/drone_control.cpp -lmavsdk
./drone_control
🔹 3. Start AI Object Detection (Anomaly Detection Layer)
bash
Copy
Edit
python Anomaly_Detection/object_detection.py
Or:

bash
Copy
Edit
g++ -o object_detection Anomaly_Detection/object_detection.cpp `pkg-config --cflags --libs opencv4`
./object_detection
🔹 4. Start Mission Control Dashboard (Mission Planning Layer)
bash
Copy
Edit
python Mission_Control/app.py
Access at: http://127.0.0.1:5000

📸 Demo Screenshots
Autonomous Flight	AI Object Detection	Mission Control
✈️ GPS Waypoints	🔍 People & Flood Detection	📡 Live Telemetry
🤖 Future Improvements
🚀 ROS Integration – Full AI automation for search & rescue
📡 5G/LoRa Connectivity – Real-time long-range drone telemetry
🛰 Satellite Image Processing – Direct ISRO/NOAA data for improved disaster mapping

👥 Team & Credits
🔹 Project Name: PerOculus
🔹 Team: Permutes
🔹 Members:

Tanishq Som – AI & UAV Control
Sumit Sharma – AI & Software Development
Manthan Dixit – IoT & Embedded Systems
Harshita Agarwal – Data Analysis & GIS
Soham Balwadkar – Web & Backend Systems
🚀 Built for Hackofiesta 6.0 (IIIT Lucknow)

📩 Contact & Support
📧 Email: tanishqsom19@gmail.com
📂 GitHub Issues: Submit a Bug
