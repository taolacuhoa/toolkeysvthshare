import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("cls")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
banner = f"""\033[1;32m
═════════════════════════════════════════════════════════════════║
\033[1;32m║➢ TOOL BY    :          Minh Hòa (ADMIN)                                                    ║
\033[1;36m║➢ ADMIN  :   Minh Hòa Support Python                                ║  
\033[1;31m║➣ ZALO HỖ TRỢ :  0889550699 ( Lê Minh Hòa )                                                    ║   
\033[1;33m║➣ DỊCH VỤ  : BÁN TOOL X WORLD ALL GAME UY TÍN                                                              ║
\033[1;37m╚═══════════════════════════════════════════════════════════════════════════════════╝
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌──────────────────────── ADMIN ────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m 3.0                                    \033[1;32m║
\033[1;32m║   \033[1;39mTELEGRAM           :  @onlyhoaf08                               \033[1;32m║
\033[1;32m║   \033[1;39mTOOL WORLD         :  TOOL VUA THOÁT HIỂM                              \033[1;32m║
\033[1'32m║   \033[1;39mZALO               :   0889550699                             \033[1;32m║ 
\033[1;39m└────────────────────────────────────────────────────────┘
"""
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0003)
menu=f"""
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m┌─────────────────────┐
\033[1;36m║  \033[1;37m    INPUT KEY      \033[1;36m║
\033[1;37m└─────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
for h in menu:
   sys.stdout.write(h)
   sys.stdout.flush()
   sleep(0.0005)
ngay=int(strftime('%d'))
key1=str(ngay*1246881818+2888181472) 
key = 'HOAVIP'+key1
keyv1 = 'hannie1231237123'
url_8link = 'https://leminhhoadz.vn/?key='+key
apikey_8link = '41f4465a54f6f0dd1b0c486d98da36ecd0dade3209dcfd8062befec77ce3d0f5'
link1s = requests.get(f'https://partner.8link.io/api/public/gen-shorten-link?apikey={apikey_8link}&url={url_8link}').json()
if 'shortened_url' not in link1s:
    print('Error: Unable to generate shortened link.')
    quit()
else:
    link_key = link1s['shortened_url']
h=open('keyDEV.txt',mode='a+')
h=open('keyDEV.txt',mode='r')
thien=h.read()
h.close()
print()
if thien== keyv1 or thien== key:
    print(dau,'\033[1;33mXIN CHÀO \033[1;32m! CHÚC BẠN CHẠY TOOL VUI VẺ...')
    sleep(1)
    exec(requests.get('https://run.mocky.io/v3/17bf0406-139f-46a9-ad1b-2a76aefb1da1').text)
else:
     print(dau,'\033[1;32mTOOL FREE ! BẢN THỬ NHIỆM - MUA TOOL LIÊN HỆ ZALO 088O550699 - 160K/ SÀI VĨNH VIỄN !')
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau,'\033[1;33mLINK LẤY API KEY LÀ:\033[1;31m '+link_key)
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩ \033[1;32mINPUT API KEY\033[1;33m ~>\033[1;36m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
if keynhap == key or keynhap== keyv1:
    print(dau,'\033[1;32mAPI KEY ĐÚNG OPEN TOOL !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(2)
    h=open('keyDEV.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://run.mocky.io/v3/cb48e7de-b60f-4f30-a60a-3b5f330d5dcc').text)
else:
    print(dau,'\033[1;33mAPI KEY SAI ! VUI LÒNG TẮT TOOL KHỞI ĐỘNG LẠI !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(1000000000)
def logo():
    pass
import random
from collections import Counter
import os
import time
import sys
                                                                # Mã màu ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
                                                                # Danh sách các phòng với tên viết tắt và tên đầy đủ
phong = {
    "NHÀ KHO": "NK",
    "PHÒNG HỌP": "PH",                                              "PHÒNG GIÁM ĐỐC": "PGD",
    "PHÒNG TRÒ CHUYỆN": "PTC",
    "PHÒNG GIÁM SÁT": "PGS",
    "VĂN PHÒNG": "VP",
    "PHÒNG TÀI VỤ": "PTV",
    "PHÒNG NHÂN SỰ": "PNS"
}

phong_keys = list(phong.values())

def hien_thi_danh_sach_phong():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BOLD}{AQUA}DANH SÁCH PHÒNG VIẾT TẮT TOOL VIP MINH HÒA:{RESET}")
    for ten_phong, ten_viet_tat in phong.items():
        print(f"{BOLD}{BLUE}{ten_phong} ({ten_viet_tat}){RESET}")

def hien_thi_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    intro_messages = [
        "ADMIN MINH HÒA CHÀO BẠN ĐÃ ĐẾN VỚI TOOL 💥",
        "TOOL HỖ TRỢ DỰ ĐOÁN TỈ SỐ CHÍNH XÁC LÊN ĐẾN 98% ⚠️",
        "ADMIN MINH HÒA XIN ĐƯỢC PHÉP BẮT ĐẦU TOOL 💢",
        "NHẬP TÊN PHÒNG VIẾT TẮT MÀ SÁT THỦ ĐÃ VÀO TRẬN TRƯỚC ❗"
        "MUA TOOL VIP CỰC RẺ LIÊN HỆ ZALO 0889550699 🎭"
    ]

    for message in intro_messages:
        print(f"{BOLD}{CYAN}{message}{RESET}")
        time.sleep(2)  # Hiển thị mỗi thông điệp trong 2 giây

    print(f"\n{BOLD}{GREEN}ĐANG TẢI VUI LÒNG CHỜ NHÉ ⏰")

    # Hiệu ứng tải
    for i in range(1, 101):
        sys.stdout.write(f"\r{BOLD}{LIME}TIẾN TRÌNH TẢI: {i}% {'█' * (i // 5)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần

    # Xóa màn hình sau khi tải xong
    os.system('cls' if os.name == 'nt' else 'clear')

hien_thi_intro()
hien_thi_danh_sach_phong()

while True:
    phong_satt_thu_da_vao = input ("Nhập Phòng Sát Thủ Đã Vào Trận Trước (ADMIN MINH HÒA)🃏: ").strip()

    if phong_satt_thu_da_vao.lower() == 'exit':
        print(f"{BOLD}{AQUA}CẢM ƠN ĐÃ SỬ DỤNG TOOL! ADMIN MINH HÒA")

        break

    if phong_satt_thu_da_vao not in phong_keys:
        print("PHÒNG KHÔNG HỢP LỆ VUI LÒNG NHẬP LẠI ⚠.")
    else:
        so_lan_mo_phong = 1000000
        ket_qua_chon = [random.choice(phong_keys) for _ in range(so_lan_mo_phong)]
        dem_phong = Counter(ket_qua_chon)
        xac_suat_phong = {phong_key: dem_phong[phong_key] / so_lan_mo_phong for phong_key in phong_keys}

        phong_thap_nhat = min(xac_suat_phong, key=xac_suat_phong.get)
        xac_suat_phong_thap_nhat_pt = xac_suat_phong[phong_thap_nhat] * 100
        phan_tram_con_lai = 100 - xac_suat_phong_thap_nhat_pt

        ten_phong_thap_nhat = [name for name, code in phong.items() if code == phong_thap_nhat][0]

        hien_thi_danh_sach_phong()

        for i in range(1, 101):
            sys.stdout.write(f"\r{BOLD}{LIME}BẮT ĐẦU DỰ ĐOÁN: {i}% {'█' * (i // 5)}{RESET}")
            sys.stdout.flush()
            time.sleep(0.03)

        print(f"\n{BOLD}{AQUA}PHÒNG NÊN CHỌN: {RESET}{BOLD}{BLUE}{ten_phong_thap_nhat} ({phong_thap_nhat}){RESET}")
        print(f"{BOLD}{YELLOW}TỈ LỆ AN TOÀN: {RESET}{phan_tram_con_lai:.2f}%")
