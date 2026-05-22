# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)
# cek stuck fungsi taruh sini - Modify stuck 13 may 2026 CAT
def cekStuckDLC(timeout_menit=1): # Default jadi 1 menit
    timeout_detik = timeout_menit * 60 
    waktu_mulai = time.time()
    
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake JME setelah download
    while True:
        if exists(Template("tpl1778659631079.png")):
            width, height = device().get_current_resolution()
            next_btn = (0.865 * width, 0.896 * height)
            allow_btn = (0.633 * width, 0.642 * height)
            touch(next_btn)
            sleep(2)
            touch(allow_btn)
            sleep(3)
            print("Berhasil masuk dan download! DLC PASSED for INKMAGINATION")
            return False 
            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f" FAILED AUT stuck selama {timeout_detik} detik.")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)
        
def dlc_ink():
    sleep(5.0)
    touch(Template(r"tpl1775628327885.png", record_pos=(-0.412, 0.168), resolution=(2400, 1080)))

dlc_ink()

def search_ink():
    
    target_icon = Template("ink.png")

    while True:
        sleep(1.0)
        pos = exists(target_icon)
        
        if pos:
            print("Inkmagination ditemukan! Melakukan Touch...")
            sleep(1.0)
            touch(pos)
            sleep(1.0)
            break # Keluar dari loop karena sudah berhasil pencet

        else:
            print("Belum ketemu, swipe ke kiri untuk mencari...")
            swipe((0.8, 0.39), (0.2, 0.39), duration=1.0)
            sleep(3)
search_ink() 

sleep(1.0)
touch(Template(r"tpl1775628647273.png", record_pos=(-0.221, -0.182), resolution=(2400, 1080)))
sleep(45.0)
wait(Template(r"tpl1775628961531.png", record_pos=(-0.308, -0.183), resolution=(2400, 1080)))
width, height = device().get_current_resolution()
hats_menu = (0.669 * width, 0.351 * height)
food_menu = (0.477*width, 0.348 * height)
Bedroom_menu = (0.305 * width, 0.351 * height)
Aliens_menu =(0.111 * width, 0.366 * height)
touch(hats_menu)
sleep(3.0)
download_btn = (0.628 * width, 0.85 * height)
later_btn = (0.392 * width , 0.85 * height)
touch(download_btn)
cekStuckDLC(1)
touch(Template(r"tpl1775628875909.png", record_pos=(-0.416, -0.185), resolution=(2400, 1080)))

