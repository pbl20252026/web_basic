# Hand Gesture Drag & Drop (Python + MediaPipe)

Ứng dụng nhận diện cử chỉ tay bằng webcam, sử dụng **MediaPipe** và **OpenCV**.  
Cho phép mô phỏng thao tác **Grab / Drag / Drop** bằng cách chụm ngón tay.

---

## 1. Giới thiệu

Dự án sử dụng thư viện MediaPipe để nhận diện bàn tay trong thời gian thực thông qua webcam.  
Khi người dùng chụm **ngón cái** và **ngón trỏ**, hệ thống sẽ nhận diện thao tác **GRAB**.  
Khi mở tay ra, hệ thống sẽ nhận diện thao tác **DROP**.

Dự án phục vụ mục đích học tập và nghiên cứu về:
- Thị giác máy tính (Computer Vision)
- Nhận diện cử chỉ tay
- Ứng dụng AI trong tương tác người – máy

---

## 2. Yêu cầu hệ thống

- Python 3.8 trở lên  
- Webcam  
- Hệ điều hành: Windows / macOS / Linux  

---

## 3. Tải project về máy

### Cách 1: Dùng Git

```bash
git clone https://github.com/pbl20252026/web_basic.git
cd web_basic

2. Cài thư viện

pip install opencv-python mediapipe numpy

3. Chạy chương trình

python hand_drag_drop.py

