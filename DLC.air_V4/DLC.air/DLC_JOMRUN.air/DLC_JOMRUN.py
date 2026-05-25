# -*- encoding=utf8 -*-
__author__ = "catur.putranto"

from airtest.core.api import *

auto_setup(__file__)

def cekStuckDLC(timeout_menit=1): # Default jadi 1 menit
    width, height = device().get_current_resolution()
    next_button =(0.875 * width, 0.873 * height)
    allow_btn = (0.615 * width, 0.671 * height)
    timeout_detik = timeout_menit * 60 
    waktu_mulai = time.time()
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake JME setelah download
    while True:
        if exists(Template("tpl1778659631079.png")):
            sleep(5)
            touch(next_button)
            sleep(1)
            touch(allow_btn)
            sleep(10)
            print("Berhasil masuk dan download! DLC PASSED for RUN ADVENTURE")
            return False 
            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f" FAILED AUT stuck selama {timeout_detik} detik.")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)
        
def rateGame():
    width, height = device().get_current_resolution()
    dontask_btn =(0.113 * width, 0.89 * height)
    touch(dontask_btn)


def DLC_JOMRUN():
    width, height = device().get_current_resolution()
    sleep(5)
    favorites_ = (0.058*width, 0.327 * height)
    JOM_menu = (0.499 * width, 0.345 * height)
    run_adv = (0.475*width, 0.802 * height)
    download_btn = (0.628 * width, 0.85 * height)
    later_btn = (0.392 * width , 0.85 * height)
    touch(favorites_)
    sleep(1)
    touch(JOM_menu)
    sleep(2)
    touch(run_adv)
    sleep(1)
    touch(download_btn)
    cekStuckDLC(1)
DLC_JOMRUN()
sleep(5)


touch(Template(r"tpl1778661133772.png", record_pos=(-0.427, -0.222), resolution=(1920, 1080)))
sleep(5)
rateGame()
    
    
