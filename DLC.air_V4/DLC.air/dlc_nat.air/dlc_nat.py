# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)

def dlc_nat():
    sleep(5.0)
    touch(Template(r"tpl1775627782872.png", record_pos=(-0.415, -0.168), resolution=(2400, 1080)))
    sleep(1.0)
    swipe(Template(r"tpl1775640283411.png", record_pos=(0.229, 0.01), resolution=(2400, 1080)), vector=[-0.1958, 0.0088])
    sleep(1.0)
    touch(Template(r"tpl1775627819688.png", record_pos=(0.396, 0.043), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1775627912284.png", record_pos=(0.31, 0.203), resolution=(2400, 1080)))
    sleep(1.0)
    touch(Template(r"tpl1775627956132.png", record_pos=(0.089, 0.152), resolution=(2400, 1080)))
    sleep(10.0)
    wait(Template(r"tpl1775628001981.png", record_pos=(-0.411, -0.182), resolution=(2400, 1080)))
    touch(Template(r"tpl1775628001981.png", record_pos=(-0.411, -0.182), resolution=(2400, 1080)))
    
    
dlc_nat()





