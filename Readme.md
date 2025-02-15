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



### 🚀 Future Enhancements
- **ROS Integration** 🤖 – Full AI automation for search & rescue missions  
- **5G/LoRa Connectivity** 🛁 – Real-time long-range UAV telemetry  
- **Satellite Image Processing** 🛰️ – Integrating ISRO/NOAA data for enhanced disaster mapping  

---

### 🎯 Team & Credits  
**Project Name:** PerOculus  
**Team:** Permutes  

👥 **Members:**  
- **Tanishq Som** – AI & UAV Control  
- **Sumit Sharma** – AI & Software Development  
- **Manthan Dixit** – IoT & Embedded Systems  
- **Harshita Agarwal** – Data Analysis & GIS  
- **Soham Balwadkar** – Web & Backend Systems  

📩 Contact & Support
📧 Email: tanishqsom19@gmail.com
📂 GitHub Issues: Submit a Bug
