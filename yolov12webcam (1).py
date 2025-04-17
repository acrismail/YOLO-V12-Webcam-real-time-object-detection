import cv2
import time
from ultralytics import YOLO

# YOLOv12 modelini yükle
model = YOLO("yolo12n.pt")

# Webcam'i başlat
cap = cv2.VideoCapture(0)  # 0, varsayılan webcam'i temsil eder

if not cap.isOpened():
    print("Webcam açılamadı!")
    exit()

# Video kaydetmek için VideoWriter ayarları
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 formatı
out = cv2.VideoWriter('output_video_yolov12.mp4', fourcc, fps, (frame_width, frame_height))

# FPS hesaplama için başlangıç zamanı
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare alınamadı, çıkılıyor...")
        break

    # Modeli çalıştır ve sonuçları al
    start_time = time.time()
    results = model(frame)
    end_time = time.time()

    # Tespit edilen nesneleri al
    detections = results[0].boxes
    num_objects = len(detections) if detections else 0

    # FPS hesapla
    fps = 1 / (end_time - prev_time)
    prev_time = end_time

    # Tespit edilen nesneleri çiz ve bilgileri ekrana yazdır
    for box, conf, cls in zip(detections.xyxy, detections.conf, detections.cls):
        x1, y1, x2, y2 = map(int, box[:4])
        label = model.names[int(cls)]  # Nesne adı
        confidence = float(conf)  # Doğruluk oranı

        # Dikdörtgen çiz
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Nesne adı ve doğruluk oranını ekle
        text = f"{label} {confidence:.2f}"
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Tespit edilen nesne sayısını ve FPS'yi ekrana yazdır
    cv2.putText(frame, f"Objects: {num_objects}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # İşlenmiş kareyi video dosyasına yaz
    out.write(frame)

    # Sonuçları göster
    cv2.imshow("Webcam - YOLOv12", frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
out.release()
cv2.destroyAllWindows()