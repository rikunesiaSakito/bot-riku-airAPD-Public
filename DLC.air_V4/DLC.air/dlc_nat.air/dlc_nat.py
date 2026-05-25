# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

<<<<<<< HEAD
#update on 25 may 2026 by CAT
def cekStuckDLC(timeout_menit=1): # Default jadi 18 detik
    timeout_detik = timeout_menit * 60 #nantinya 18 detik, cuma untuk tes percobaan di DINO DLC
    waktu_mulai = time.time()
    
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake gambar dino yang nyari tulang, jika bisa masuk artinya DLC berhasil di download jika tidak brti anggap stuck!
    while True:
        if exists(Template("tpl1779690738724.png")):
            print("✅ Berhasil masuk dan download!")
            return False 
            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f"🚨 STUCK! Melebihi batas {timeout_detik} detik.")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)

def dlc_nat():
    width, height = device().get_current_resolution()
    download_bt = (0.591 * width, 0.838 * height)
=======
def dlc_nat():
>>>>>>> 026a6935b6e2a2a753cdcb89e30a7c6b9b1c3dc3
    sleep(5.0)
    touch(Template(r"tpl1775627782872.png", record_pos=(-0.415, -0.168), resolution=(2400, 1080)))
    sleep(1.0)
    swipe(Template(r"tpl1775640283411.png", record_pos=(0.229, 0.01), resolution=(2400, 1080)), vector=[-0.1958, 0.0088])
    sleep(1.0)
<<<<<<< HEAD
    touch(Template("tpl1779692686359.png"))
    sleep(3)
    touch(Template("tpl1779692709431.png"))
    sleep(5)
    touch(download_bt)
    cekStuckDLC(1)
    sleep(5)
=======
    touch(Template(r"tpl1775627819688.png", record_pos=(0.396, 0.043), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1775627912284.png", record_pos=(0.31, 0.203), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1775627956132.png", record_pos=(0.089, 0.152), resolution=(2400, 1080)))
    sleep(10.0)
>>>>>>> 026a6935b6e2a2a753cdcb89e30a7c6b9b1c3dc3
    wait(Template(r"tpl1775628001981.png", record_pos=(-0.411, -0.182), resolution=(2400, 1080)))
    touch(Template(r"tpl1775628001981.png", record_pos=(-0.411, -0.182), resolution=(2400, 1080)))
    
    
dlc_nat()





