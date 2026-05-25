# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

def dlc_ls():
    sleep(5.0)
    touch(Template(r"tpl1775619125221.png", record_pos=(-0.414, -0.084), resolution=(2400, 1080)))
    sleep(1.0)
    
dlc_ls()

def search_ls():

    target_icon = Template(r"tpl1775619782324.png", record_pos=(0.0, 0.0), resolution=(1080, 1920))

    while True:
        sleep(1.0)
        pos = exists(target_icon)
        
        if pos:
            print("Lets Story ditemukan! Melakukan Touch...")
            sleep(1.0)
            touch(pos)
            sleep(1.0)
            break # Keluar dari loop karena sudah berhasil pencet

        else:
            print("Belum ketemu, swipe ke kiri untuk mencari...")
            swipe((0.8, 0.39), (0.2, 0.39), duration=1.0)
            sleep(3)
search_ls() 
touch(Template(r"tpl1775620280768.png", record_pos=(-0.065, 0.203), resolution=(2400, 1080)))
sleep(5.0)
touch(Template(r"tpl1775620351062.png", record_pos=(-0.415, -0.18), resolution=(2400, 1080)))
touch(Template(r"tpl1775620385089.png", record_pos=(-0.416, -0.176), resolution=(2400, 1080)))



