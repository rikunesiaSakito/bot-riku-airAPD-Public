# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *

auto_setup(__file__)
#suggest at the 1st language set to EN
#DLC dino - harus udah main tutorial selesai dulu, Dino OK, WE OK may 05 2026

using("dlc_dino.air") 
using("dlc_we.air")
using ("DLC_JOMRUN.air")# JOM rund adventure anyar 13 may 2025
using("dlc_sw.air")
#using("dlc_ls.air")
#using("dlc_kin.air")
using("dlc_nat.air")
using("dlc_ink.air")
import dlc_dino
import dlc_we
import DLC_JOMRUN
import dlc_sw
#import dlc_ls not available
import dlc_nat
import dlc_ink
import dlc_kin

dlc_dino()
dlc_we()
DLC_JOMRUN()
dlc_sw()
#dlc_ls()
dlc_kin()
dlc_nat()
dlc_ink()
