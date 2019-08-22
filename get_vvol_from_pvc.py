#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Written by Jon Owings
# GitHub: https://github.com/2vcps
# Email: owings@purestorage.com
# Website: http://blog.2vcps.io
#
# Note: Example code For testing purposes only
#
# This code has been released under the terms of the Apache-2.0 license
# http://opensource.org/licenses/Apache-2.0

from kubernetes import client, config
import purestorage as ps
import pure_pks_vvol as ppv
import argparse
# Never do this in prod. SSL warning are there for a reason.
import urllib3
urllib3.disable_warnings()

def get_args():
    """
    Require a PVC name

    -p PVCNAME
    --pvcname PVCNAME
    """
    parser = argparse.ArgumentParser()

# add long and short argument
    parser.add_argument("--pvcname", "-p", help="Get the vVol name from PVC")

# read arguments from the command line
    args = parser.parse_args()
    return args.pvcname

#pvc_name = input("Enter PVC Name: ")
pvc_name = get_args()
def get_vvols_name(pvc_name):
    if(pvc_name):
        pv_name, vmw_path, pvc_array, pv_array = ppv.k8s_gather(pvc_name)
        vvolx = ppv.pure_gather(vmw_path)
    else:
        vvolx = "bad"
    return vvolx

vvol_name = get_vvols_name(pvc_name)
print(vvol_name)
