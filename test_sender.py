import requests
import json

# Địa chỉ Server Flask đang chạy trên máy bạn
SERVER_URL = "http://127.0.0.1:5000/upload"

# 1. Đường dẫn tới file ảnh test
IMAGE_PATH = "test_pcba.jpg" 

# 2. Giả lập Mảng Lỗi Matrix (Ví dụ: Lưới 3x3, có 2 ô bị lỗi ở vị trí (0,1) và (2,0))
matrix_mock = [
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# 3. Đóng gói và gửi HTTP POST request giả lập ESP32-S3
try:
    with open(IMAGE_PATH, 'rb') as img_file:
        files = {'image': img_file}
        data = {'matrix': json.dumps(matrix_mock)}
        
        print("Đang gửi dữ liệu test lên Server...")
        response = requests.post(SERVER_URL, files=files, data=data)
        
        print("Mã phản hồi từ Server:", response.status_code)
        print("Nội dung phản hồi:", response.json())

except Exception as e:
    print("Lỗi khi gửi dữ liệu:", e)