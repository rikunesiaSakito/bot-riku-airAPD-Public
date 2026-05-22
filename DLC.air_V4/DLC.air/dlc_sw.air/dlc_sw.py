# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *
auto_setup(__file__)
#modify 13 may 2026 CAT
def cekStuckDLC(timeout_menit=1): # Default jadi 1 menit
    timeout_detik = timeout_menit * 60 
    waktu_mulai = time.time()
    print(f"--- MONITORING SINGKAT: {timeout_detik} detik ---")
    #coba pake JME setelah download
    while True:
        if exists(Template(r"tpl1778664787962.png", record_pos=(0.015, -0.219), resolution=(1920, 1080))):

            sleep(5)
            print("Berhasil masuk dan download! DLC PASSED for STAR WARS DE LANGUAGE")
            return False 
            
        durasi_berjalan = time.time() - waktu_mulai
        
        # Jika durasi sudah lewat dari batas detik
        if durasi_berjalan > timeout_detik:
            print(f" FAILED AUT stuck selama {timeout_detik} detik.")
            return True 
            
        print(f"⏳ Menunggu... ({int(durasi_berjalan)}s / {int(timeout_detik)}s)")
        sleep(1)
def new_parental_set():
    width, height = device().get_current_resolution()
    tri_year = (0.245 * width, 0.39 * height)
    gender =(0.572 * width, 0.421 * height)
    minutes_60 =(0.798 *width, 0.49 * height)
    nxt_button =(0.884* width, 0.872 * height)
    next_icon =(0.946* width, 0.908 * height)
    fieldname =(0.485 * width, 0.874 * height)
    touch(tri_year)
    touch(gender)
    touch(minutes_60)
    touch(nxt_button)
    sleep(1)
    text("rikuenesiaSakitos")
    touch(nxt_button)
    

def dlc_sw():
    touch(Template(r"tpl1775638583740.png", record_pos=(-0.416, -0.169), resolution=(2400, 1080)))
    sleep(5.0)
    link = "https://qr.kinder.com/VC368"

    shell(f'am start -a android.intent.action.VIEW -d "{link}"')
    sleep(10)
    touch(Template(r"tpl1775618322860.png", record_pos=(0.015, 0.026), resolution=(2400, 1080)))
    sleep(15.0)
    width, height = device().get_current_resolution()
    letsGo = (0.501* width, 0.874 * height)
    touch(letsGo)
    sleep(3.0)

dlc_sw()

touch(Template(r"tpl1775640011605.png", record_pos=(-0.414, -0.083), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942354699.png", record_pos=(0.309, -0.178), resolution=(2400, 1080)))
sleep(2.0)
touch(Template(r"tpl1774942398451.png", record_pos=(0.275, -0.048), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942417325.png", record_pos=(0.278, 0.172), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942417325.png", record_pos=(0.278, 0.172), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942417325.png", record_pos=(0.278, 0.172), resolution=(2400, 1080)))
sleep(7.0)
new_parental_set()
touch(Template(r"tpl1774942504082.png", record_pos=(-0.412, 0.194), resolution=(2400, 1080)))
sleep(1.0)
swipe(Template(r"tpl1774942551101.png", record_pos=(-0.03, 0.012), resolution=(2400, 1080)), vector=[-0.0126, -0.3643])
sleep(1.0)
swipe(Template(r"tpl1774942593279.png", record_pos=(-0.115, -0.019), resolution=(2400, 1080)), vector=[-0.0187, -0.4041])
sleep(1.0)
touch(Template(r"tpl1778665492280.png", record_pos=(0.265, 0.014), resolution=(1920, 1080)))
sleep(1.0)
touch(Template(r"tpl1774942681303.png", record_pos=(-0.412, -0.189), resolution=(2400, 1080)))
sleep(3.0)
touch(Template(r"tpl1774942719866.png", record_pos=(-0.417, -0.169), resolution=(2400, 1080)))
sleep(1.0)
touch(Template(r"tpl1778664514250.png", record_pos=(-0.001, -0.016), resolution=(1920, 1080)))


sleep(1.0)
touch(Template(r"tpl1774942787076.png", record_pos=(-0.25, 0.202), resolution=(2400, 1080)))
sleep(1.0)
width, height = device().get_current_resolution()
download_btn = (0.628 * width, 0.85 * height)
later_btn = (0.392 * width , 0.85 * height)
touch(download_btn)
cekStuckDLC(1)
wait(Template(r"tpl1774942878956.png", record_pos=(0.451, 0.17), resolution=(2400, 1080)))
touch(Template(r"tpl1774942894676.png", record_pos=(-0.415, -0.185), resolution=(2400, 1080)))
sleep(5.0)

