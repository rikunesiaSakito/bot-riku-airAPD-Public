# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *
import time

auto_setup(__file__)

# cek stuck fungsi taruh sini - Modify stuck 05 may 2026 CAT


def cekStuckDLC(timeout_menit=1): # Default jadi 18 detik
    timeout_detik = timeout_menit * 60 #nantinya 18 detik, cuma untuk tes percobaan di DINO DLC
    waktu_mulai = time.time()
    
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake gambar dino yang nyari tulang, jika bisa masuk artinya DLC berhasil di download jika tidak brti anggap stuck!
    while True:
        if exists(Template("tpl1777966735860.png")):
            print("✅ Berhasil masuk dan download!")
            return False 
            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f"🚨 STUCK! Melebihi batas {timeout_detik} detik.")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)

def dlc_dino():
    stop_app("com.ferrero.applayduGP")
    start_app("com.ferrero.applayduGP")
    width, height = device().get_current_resolution()
    collection_=(0.061 * width, 0.124 * height)
    triceratops = (0.518 * width, 0.435 * height)
    sleep(20)
    wait(Template(r"tpl1773305966050.png", record_pos=(-0.415, -0.085), resolution=(2400, 1080)))
    touch(collection_)
    sleep(1.0)
    touch(triceratops)
    sleep(1.0)
    touch(Template(r"tpl1773306107271.png", record_pos=(-0.25, 0.199), resolution=(2400, 1080)))
    sleep(3.0)
    touch(Template(r"tpl1773306141287.png", record_pos=(0.316, 0.101), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1773306172308.png", record_pos=(-0.002, 0.184), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1773306194070.png", record_pos=(-0.006, 0.154), resolution=(2400, 1080)))
    sleep(1)
    cekStuckDLC(1)
    while exists(Template(r"tpl1775633265625.png")): sleep(1)
    
    
    wait(Template(r"tpl1773306367073.png", record_pos=(-0.416, -0.186), resolution=(2400, 1080)), timeout=120)
    touch(Template(r"tpl1773306380474.png", record_pos=(-0.416, -0.186), resolution=(2400, 1080)))
    sleep(2.0)
    touch(Template(r"tpl1773306441459.png", record_pos=(-0.415, -0.179), resolution=(2400, 1080)))

dlc_dino()

