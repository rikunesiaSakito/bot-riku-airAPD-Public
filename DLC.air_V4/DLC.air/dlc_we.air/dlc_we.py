# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)
# cek stuck fungsi taruh sini - Modify stuck 05 may 2026 CAT - Script error if stuck occurs perlu tambahan catch error atau lakukan jika udah stuck gara scirpt tetap berjalan

def cekStuckDLC(timeout_menit=1): # Default jadi 6 detik
    timeout_detik = timeout_menit * 60 #nantinya 18 detik, cuma untuk tes percobaan di DINO DLC
    waktu_mulai = time.time()
    
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake gambar dino yang nyari tulang, jika bisa masuk artinya DLC berhasil di download jika tidak brti anggap stuck!
    while True:
        if exists(Template("Word_explorer.png")):
            print("Berhasil masuk dan download! DLC aman")
            return False 
        #cek jika ada no internet pop up print juga stuck , modify - 13 may 2026 Cat
        
        if exists(Template(r"tpl1778654883303.png", record_pos=(-0.002, -0.048), resolution=(1920, 1080))):
            width, height = device().get_current_resolution()
            Try_again_button = (0.49 * width, 0.82 * height)
            touch(Try_again_button)
            sleep(3)
            touch(Try_again_button)
            sleep(5)
            print("FAILED No internet connection keep appear!")
            return True
            

            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f" FAILED Time Out Longer than 1 Minutes")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)
        
def dlc_we():
    sleep(5.0)
    wait(Template(r"tpl1773306717664.png", record_pos=(-0.414, 0.165), resolution=(2400, 1080)))
    touch(Template(r"tpl1773306724135.png", record_pos=(-0.413, 0.165), resolution=(2400, 1080)))
    sleep(1.0)
dlc_we()
   
def search_we():  
    target_icon = Template("tpl1777969312000.png")
    while True:
        sleep(1.0)
        pos = exists(target_icon)
        
        if pos:
            print("Word Explorer ditemukan! Melakukan Touch...")
            sleep(1.0)
            touch(pos)
            sleep(1.0)
            break # Keluar dari loop karena sudah berhasil pencet

        else:
            print("Belum ketemu, swipe ke kiri untuk mencari...")
            swipe((0.8, 0.39), (0.2, 0.39), duration=1.0)
            sleep(3)
search_we()           

print("Berhasil masuk, sekarang klik tombol selanjutnya...")
sleep(2.0) 
width, height = device().get_current_resolution()
download_btn = (0.628 * width, 0.85 * height)
later_btn = (0.392 * width , 0.85 * height)

touch(download_btn)
sleep(1)
cekStuckDLC(1)
wait(Template(r"tpl1773392431216.png", record_pos=(0.467, 0.182), resolution=(2400, 1080)))
touch(Template(r"tpl1773392440750.png", record_pos=(0.468, 0.18), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1773392480858.png", record_pos=(-0.426, -0.186), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1773392512166.png", record_pos=(-0.42, -0.186), resolution=(2400, 1080)))





