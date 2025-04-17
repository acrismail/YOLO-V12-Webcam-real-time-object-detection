# YOLO-V12-Webcam-real-time-object-detection
YOLOv12 ve OpenCV kullanarak web kamerası üzerinden FPS izleme ile algılama yapan gerçek zamanlı nesne algılama projesi

## Özellikler
- YOLOv12 ile gerçek zamanlı nesne tespiti
- Webcam üzerinden canlı video işleme
- FPS (Saniyedeki Kare Sayısı) ölçümü ve ekranda gösterimi
- Tespit edilen nesne sayısının takibi
- Her nesne için doğruluk oranı (confidence) gösterimi
- Tespit edilen nesneler için sınıf etiketi ve dikdörtgen çizimi
- İşlenmiş videonun kaydedilmesi

## Teknik Detaylar
- Model: YOLOv12 (Ultralytics)
- Programlama Dili: Python
- Kullanılan Kütüphaneler: OpenCV, Ultralytics

## Çıktı Bilgileri
Sistem, ekranda şunları gösterir:
- Tespit edilen nesneler ve dikdörtgen kutuları
- Nesne sınıf etiketleri
- Her tespit için doğruluk oranı
- Anlık FPS değeri
- Toplam tespit edilen nesne sayısı

## Gereksinimler
- Python 3.x
- OpenCV
- Ultralytics
- Webcam

## Kullanım
1. Depoyu klonlayın.
2. Gerekli kütüphaneleri yükleyin.
3. Python dosyasını çalıştırın.
4. Uygulamadan çıkmak için 'q' tuşuna basın.

İşlenmiş video, proje dizininde `output_video_yolov12.mp4` olarak kaydedilecektir.

## Not
Bu proje, YOLOv12 ile gerçek zamanlı nesne tespiti ve performans ölçümü uygulamasını örneklemektedir. Bilgisayarla görü ve nesne tespiti alanında çeşitli uygulamalar için temel oluşturabilir.
