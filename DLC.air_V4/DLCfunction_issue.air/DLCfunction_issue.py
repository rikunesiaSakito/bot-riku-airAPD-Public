# -*- encoding=utf8 -*-
__author__ = "catur.putranto"

from airtest.core.api import *
import time
auto_setup(__file__)


def cekStuckDLC(timeout_menit=0.3): # Default jadi 18 detik
    timeout_detik = timeout_menit * 60 #nantinya 18 detik, cuma untuk tes percobaan di DINO DLC
    waktu_mulai = time.time()
    
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake gambar dino yang nyari tulang, jika bisa masuk artinya DLC berhasil di download jika tidak brti anggap stuck!
    while True:
        if exists(Template(r"tpl1777966735860.png", record_pos=(0.008, 0.059), resolution=(1920, 1080)))
:
            print("✅ Berhasil sebelum timeout!")
            return False 
            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f"🚨 STUCK! Melebihi batas {timeout_detik} detik.")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)
cekStuckDLC(0.3)