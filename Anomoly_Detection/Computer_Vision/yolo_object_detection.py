import cv2
import torch
import numpy as np
import time
import threading
from ultralytics import YOLO
from datetime import datetime


model = YOLO("yolov8n.pt")  


cv2.setNumThreads(1)
VIDEO_SOURCE = "Indoor_Test_Flight.mp4" 


CONF_THRESHOLD = 0.5


COLORS = np.random.randint(0, 255, size=(80, 3), dtype="uint8")


cap = cv2.VideoCapture(VIDEO_SOURCE)
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()


log_filename = "../Detection_Logs/detections_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"
log_file = open(log_filename, "w")
log_file.write("Timestamp,Object,Confidence,X,Y,Width,Height\n")


def log_detection(label, conf, x, y, w, h):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp},{label},{conf:.2f},{int(x)},{int(y)},{int(w)},{int(h)}\n"
    log_file.write(log_entry)
    print(log_entry.strip())

def process_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        
        results = model(frame)


        for result in results:
            for det in result.boxes.data.tolist():  
                x1, y1, x2, y2, conf, class_id = det
                if conf > CONF_THRESHOLD:
                    label = model.names[int(class_id)]
                    color = [int(c) for c in COLORS[int(class_id) % len(COLORS)]]

                    
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                    cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                    log_detection(label, conf, x1, y1, x2-x1, y2-y1)

       
        cv2.imshow("YOLOv8 Object Detection", frame)

    
        cv2.imwrite(f"Anomaly_Detection/Detection_Logs/frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg", frame)

        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


thread = threading.Thread(target=process_frames)
thread.start()


cap.release()
cv2.destroyAllWindows()
log_file.close()
