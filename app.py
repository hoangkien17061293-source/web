from flask import Flask, request, render_template, jsonify
import os
import json
import time

app = Flask(__name__)

# Thư mục lưu trữ ảnh thô do ESP32-S3 gửi lên
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Biến toàn cục lưu trạng thái dữ liệu mới nhất
latest_data = {
    "image_url": "",
    "matrix": [],
    "timestamp": 0
}

@app.route('/')
def index():
    # Trang giao diện Web chính
    return render_template('index.html')

# API tiếp nhận dữ liệu từ ESP32-S3
@app.route('/upload', methods=['POST'])
def upload():
    global latest_data
    
    # 1. Kiểm tra và lưu file ảnh từ ESP32-S3
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "No image file"}), 400
        
    file = request.files['image']
    timestamp = int(time.time())
    filename = f"pcba_{timestamp}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # 2. Nhận chuỗi Matrix lỗi từ ESP32-S3
    matrix_str = request.form.get('matrix', '[]')
    try:
        matrix_data = json.loads(matrix_str)
    except:
        matrix_data = []

    # 3. Cập nhật dữ liệu mới nhất
    latest_data = {
        "image_url": f"/static/uploads/{filename}",
        "matrix": matrix_data,
        "timestamp": timestamp
    }

    print(f"[SUCCESS] Nhan anh: {filename} | Matrix: {matrix_data}")
    return jsonify({"status": "success"}), 200

# API để giao diện Web liên tục hỏi dữ liệu mới (Polling)
@app.route('/get_latest', methods=['GET'])
def get_latest():
    return jsonify(latest_data)

if __name__ == '__main__':
    # Chạy server ở IP 0.0.0.0 để các thiết bị cùng mạng WiFi kết nối được
    app.run(host='0.0.0.0', port=5000, debug=True)