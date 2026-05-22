# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)
def dlc_kin():
    sleep(5.0)
    touch(Template(r"tpl1775627230860.png", record_pos=(-0.412, -0.086), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1775627271852.png", record_pos=(0.216, 0.007), resolution=(2400, 1080)))
    wait(Template(r"tpl1775627334202.png", record_pos=(0.125, 0.201), resolution=(2400, 1080)))
    touch(Template(r"tpl1775627334202.png", record_pos=(0.125, 0.201), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1775627448732.png", record_pos=(0.087, 0.154), resolution=(2400, 1080)))
    while exists(Template(r"tpl1775633265625.png")): sleep(1)
    sleep(1.0)
    wait(Template(r"tpl1775627544479.png", record_pos=(0.452, 0.175), resolution=(2400, 1080)))
    touch(Template(r"tpl1775627558177.png", record_pos=(-0.421, -0.182), resolution=(2400, 1080)))
    
dlc_kin()



