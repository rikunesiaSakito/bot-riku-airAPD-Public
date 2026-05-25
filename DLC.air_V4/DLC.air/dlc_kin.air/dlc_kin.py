# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *
auto_setup(__file__)

def cekStuckDLC(timeout_menit=1): # Default jadi 18 detik
    timeout_detik = timeout_menit * 60 #nantinya 18 detik, cuma untuk tes percobaan di DINO DLC
    waktu_mulai = time.time()
    
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake gambar dino yang nyari tulang, jika bisa masuk artinya DLC berhasil di download jika tidak brti anggap stuck!
    while True:
        if exists(Template("tpl1779694664855.png")):
            print("✅ Berhasil masuk dan download!")
            return False 
            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f"🚨 STUCK! Melebihi batas {timeout_detik} detik.")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)
def dlc_kin():
    width, height = device().get_current_resolution()
    emo_menu = (0.478 * width, 0.813 * height)
    download_btn = (0.612 * width, 0.847 * height)
    sleep(5.0)
    touch(Template(r"tpl1775627230860.png", record_pos=(-0.412, -0.086), resolution=(2400, 1080)))
    sleep(1.0)
    swipe((0.8, 0.39), (0.2, 0.39), duration=1.0)
    touch(Template(r"tpl1775627271852.png", record_pos=(0.216, 0.007), resolution=(2400, 1080)))
    wait(Template("tpl1779694455439.png"))
    touch(emo_menu)
    sleep(1.0)
    touch(download_btn)
    cekStuckDLC(1)
    sleep(1.0)
    wait(Template(r"tpl1775627544479.png", record_pos=(0.452, 0.175), resolution=(2400, 1080)))
    touch(Template(r"tpl1775627558177.png", record_pos=(-0.421, -0.182), resolution=(2400, 1080)))
    
dlc_kin()



