os.system("pip install pytube")
from pytube import YouTube
import threading,base64
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
import os, sys
import os,sys
import pywifi
from requests import session
from colorama import Fore, Style
import requests, random, re
from random import randint
import requests,pystyle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from datetime import date
from datetime import datetime
from time import sleep
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
from tqdm import tqdm
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
def loading_bar():
    for _ in tqdm(range(100), desc="Đang tải", bar_format=f"{Fore.WHITE}{{l_bar}}{{bar}}{{r_bar}}{Fore.RESET}", ncols=100):
        sleep(0.1)
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.1)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
weather_description = get_weather()
System.Clear()
#màu

print(f"""
\033[1;34m╔═══════════╗
\033[1;36m║▇◤▔▔▔▔▔▔▔◥▇║
\033[1;36m║▇▏◥▇◣┊◢▇◤▕▇║
\033[1;36m║▇▏▃▆▅▎▅▆▃▕▇║
\033[1;36m║▇▏╱▔▕▎▔▔╲▕▇║
\033[1;36m║▇◣◣▃▅▎▅▃◢◢▇║
\033[1;36m║▇▇◣◥▅▅▅◤◢▇▇║
\033[1;36m║▇▇▇◣╲▇╱◢▇▇▇║
\033[1;36m║▇▇▇▇◣▇◢▇▇▇▇║
\033[1;34m╚═══════════╝
\033[1;97mTool By: \033[1;32mAnhhCode            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mAnhCode\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mhttps://www.facebook.com/profile.php?id=61570408533569
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/shareanhcode🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
""")
def download_video(url, NamVN):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=NamTool)
        print(f"{luc}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mVideo đã được tải xuống thành công!")
    except Exception as e:
        print("Đã xảy ra lỗi:", str(e))
video_url = input(f"{trang}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập link video youtube cần tải:{vang}")
loading_bar()
NamTool = "video_yt_download_by_atom"
print("Tool by Anhcode")
download_video(video_url, NamTool)
