# -*- encoding=utf8 -*-
__author__ = "catur.putranto"

from airtest.core.api import *
import requests
import json
import time
auto_setup(__file__)

# 1. Buat Variable dari kosong , untuk menghitung waktu di home screen nantinya, jika lebih dari 50 menit suspect crash saja , jika tidak lanjut tap tap
waktu_mulai_stuck = None 

def cekCrash():
    MATTERMOST_URL = "https://chat.gameloft.org/hooks/4sd5gz86a7n73e8bi5cpsde7tr"
    _app = "com.ferrero.applayduGP"
    
    #shell("am force-stop com.ferrero.applayduGP")
    result = shell("dumpsys window | grep mCurrentFocus") #bikin variable cek jika di homescreen nantinya variable 
    #pastikan pake strip setiap kali menggunakan sheel untuk membersihkan kiri dan kanan text.
    if "launcher" in result.lower():
        dev_merk = shell("getprop ro.product.manufacturer").strip() # merk hape digunakan 
        dev_model = shell("getprop ro.product.model").strip() # ambil model hape
        dev_firmware = shell ("getprop ro.build.version.release").strip() # ambil firmware
        print("Saat ini Hape Anda sedang berada di homescreen, kemungkinan CRASH!!" + dev_merk + " " +  dev_model + " Firmware  " + dev_firmware)
        # 28 may 2026 - parameter logcat shell jika menangkap error ganti E bukan D
        logAndro = shell('logcat -d -v brief *:D | grep com.ferrero.applayduGP | tail -n 5')
        log_aman = logAndro.replace("\\", "/").replace('"', "'").replace("|", "/")
        log_aman = log_aman.replace("[", "(").replace("]", ")")
        
        # Potong per baris agar tidak melar ke samping
        baris_log = log_aman.split("\n")
        baris_rapi = []
        for b in baris_log:
            if b.strip():
                potong = b.strip()[:80] + "..." if len(b.strip()) > 80 else b.strip()
                baris_rapi.append(potong)
        
        log_bersih_tabel = "<br>".join(baris_rapi)
        
        # Bungkus hasil akhir dengan satu petik terbalik
        if log_bersih_tabel.strip() != "":
            log_bersih_tabel = f"`{log_bersih_tabel}`"
        else:
            log_bersih_tabel = "Tidak ini bukan crash (Logcat bersih)"
        
        #percobaan bikin error pembagian dengan 0 atau bikin saja ndak ada gambar
        #try:
            #1/0
       # except Exception:
            #log_asli = traceback.format_exc()
       # if "NoneType" in log_asli or log_asli.strip() == "None: None" or log_asli.strip() == "None":
                #log_bersih_tabel = f"Bot murni stuck/diam selama {durasi:.1f} detik."
        #else:
            #log_aman_path = log_asli.replace("\\", "/")
                # 2. Ganti tanda petik dua (") menjadi petik satu (') agar f-string tidak bocor
            #log_tanpa_petik = log_aman_path.replace('"', "'")
                # 3. Ganti enter (\n) menjadi <br> agar tetap di dalam kotak tabel
            #log_bersih_tabel = log_tanpa_petik.replace("\n", "<br>")
                
        payload = {
            "username": "RikuCrashBOT",
            "text": (
                    f"### 🚨 CRASH DETECTED!\n"
                    f"| Info | Detail |\n"
                    f"| :--- | :--- |\n"
                    f"| **Device** | {dev_merk.upper()} {dev_model} |\n"
                    f"| **Android** | Version {dev_firmware} |\n"
                    f"| **Status** | Segera Cek, Kemungkinan Crash! |\n"
                    f"| **Log Error** | `{log_bersih_tabel}` |"  # Gunakan variabel yang sudah bersih
                )
        }
        requests.post(MATTERMOST_URL, json=payload)
            
            # --- RESTART LOGIC ---
        stop_app(_app) # paksa AUT berhenti
        sleep(2) # kasih sleep
        start_app(_app) # paksa AUT jalan lagi
        sleep(25) # Tunggu loading game
            
        waktu_mulai_stuck = None       
        return True # Masih di launcher - agar tidak sembarang clikc
        
    else:
        # print("Aman: Masih di dalam Game")
        return False
# seperti biasa buat dictionary dulu, biar gampang modif kalo ada icon baru di coordinat lain

# modif jam 16.00 04 may 2026
def INK_():
    width, height = device().get_current_resolution()
    target = (0.305 * width, 0.082 * height)
    backkey = (0.061 * width, 0.109 * height)
    hatsMenu = (0.663 * width, 0.363 * height)
    downloadButton = (0.559 * width , 0.882 * height)
    sleep(10)
    touch(target)
    sleep(3)
    #touch(backkey)
    #sleep(2)
    touch(hatsMenu)
    sleep(3)
    touch(downloadButton)
    

    
    


#fungsi menu2 yang diakses di icon collection
def COLS(width, height):
    reset_ = (0.051 * width, 0.132 * height)
    icon = {
        "icon_COL" : (0.185 * width, 0.191 * height),
        "icon_natoons" : (0.263 * width, 0.203 * height),
        "icon_vet" : (0.354 * width, 0.188 * height),
        "icon_space" : (0.434 * width, 0.197 * height),
        "icon_unicorn" : (0.52 * width, 0.174 * height),
        "icon_teamRacing" : (0.598 * width, 0.203 * height),
        "icon_Dino" : (0.679 * width, 0.212 * height),
        "icon_funAnimal" : (0.77 * width, 0.185 * height)
    }
    for name, coordinat in icon.items():
        # CEK DULU sebelum klik
        if cekCrash(): 
            break 
            
        print(f"Klik Sub-menu: {name}")
        touch(coordinat)
        #Taruh sini untuk menu2 yang mau di explore terkait panda
        if (name == "icon_natoons"):
            subs("panda_natoo")
            touch(reset_)
            sleep(3)
         #Taruh sini untuk menu2 yang mau di explore terkait Hiku
        elif(name == "icon_vet"):
            subs("hiku_vet")
            touch(reset_)
            sleep(3)
            #Taruh sini untuk menu2 yang mau di explore terkait Space
        elif(name == "icon_space"):
            subs("Space_Jet")
            touch(reset_)
            sleep(3)
            #Taruh sini untuk menu2 yang mau di explore terkait unicorn
        elif(name == "icon_unicorn"):
            subs("Fantasys")
            touch(reset_)
            sleep(3)
            #Taruh sini untuk menu2 yang mau di explore terkait Team Racing
        elif(name == "icon_teamRacing"):
            subs("TeAmRacing")
            touch(reset_)
            sleep(3)
            #Taruh sini untuk menu2 yang mau di explore terkait Dino
        elif(name == "icon_Dino"):
            subs("Dino")
            touch(reset_)
            sleep(3)
            #Taruh sini untuk menu2 yang mau di explore terkait Fun Animal
        elif(name == "icon_funAnimal"):
            subs("FUNtoys")
            touch(reset_)
            sleep(3)
        
            
            
            
            
        sleep(5)
        # fungsi di dalem collection (pojok atas)
def subs(name_subs):
    width, height = device().get_current_resolution()
    daftar = {
        "panda_natoo" : (0.51 * width, 0.48 * height),
        "hiku_vet" : (0.275 * width, 0.824 * height),
        "Space_Jet" : (0.25 * width, 0.774 * height),
        "Fantasys" :(0.291 * width, 0.807 * height),
        "TeAmRacing" : (0.291 * width, 0.807 * height),
        "Dino": (0.291 * width, 0.807 * height),
        "FUNtoys" : (0.291 * width, 0.807 * height)
        
    }
    
    if name_subs in daftar:
        print(f"--- Masuk ke detail sub-menu: {name_subs} ---")
        #lebih cepat pake dictionary tinggal spesifikasikan terlebih dahulu
        touch(daftar[name_subs])
        sleep(5)
    else:
        print("TIDAK DITEMUKAN!!!")
    
#modif di jam 13.32 Hari senin 04 may 2026
def DLCInk():
    width, height = device().get_current_resolution()
    for i in range (8):
        target = exists(Template("tpl1777875780387.png"))# harus di masukkan dalam loop
        if (target):
            print("Target Di temukan")
            touch(target)
            sleep(4)
            INK_()
            break
        else:
            posX = 0.42 * width
            posY = 0.414 * height
            swipe((posX, posY), (posX - (0.3 * width), posY))
            print("Target belum terliat!!!!!! lakukan scroll")
            sleep(3)

#fungsi di dalem moregames    
#modif di jam 09.12 05 May 2026, menu more games

def MoreGames(name_sub):
    width, height = device().get_current_resolution()
    menu  = {
        "Food_Quest" : Template("tpl1777947292054.png"),
        "Fantasy_Story" : Template("tpl1777947306622.png"),
        "INkmagination" : Template("tpl1777875780387.png")


    }
    if name_sub in menu:
        if name_sub == "INkmagination":
            DLCInk()

        
        

def AImenu():
    width, height = device().get_current_resolution()
    # Pindahkan dictionary ke sini agar lebih rapi
    left_menu = {
        "collection_menu" : (0.053 * width, 0.127 * height),
        "Favorite_menu"   : (0.073 * width, 0.312 * height),
        "Toys_menu"       : (0.071 * width, 0.498 * height),
        "Avatar"          : (0.071 * width, 0.677 * height),
        "Games"           : (0.058 * width, 0.863 * height)
    }

    while True:  #LOOPING ABADI ini
        print("\n--- Memulai Putaran Testing Baru ---")
        
        for name, coordinat in left_menu.items():
            # Jika di Home Screen, cekCrash() akan return True (karena sedang standby/restart)
            if cekCrash():
                print(f"⚠️ Sedang Recovery... Skip menu {name}")
                # Pakai break untuk keluar dari 'for' dan mengulang dari 'while'
                break 
            
            print(f"Klik Menu Utama: {name}")
            touch(coordinat)
            sleep(4)
            
            if name == "collection_menu":
                COLS(width, height)
            elif name == "Games":
                MoreGames("INkmagination")
        
        print("✅ Putaran selesai atau terjadi reset. Mengulang...")
        sleep(2) # Kasih napas 2 detik sebelum mulai putaran baru

# Eksekusi
AImenu()