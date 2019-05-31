from kubernetes import client, config
import purestorage as ps
import pure_pks_vvol as ppv

# Never do this in prod. SSL warning are there for a reason.
import urllib3
urllib3.disable_warnings()

snap_name = input("Enter Snap or Volume Name: ")
suffix_name = input("We require a suffix for the new name: ")
dest_name = snap_name[:-2] + suffix_name

new_pvc_vol = ppv.pure_new_vol(snap_name, dest_name)
temp_name = new_pvc_vol
temp_name = str(temp_name)
list_name = temp_name.split(",")
list_name = list_name[3].strip("'name': ")
new_vvol = list_name
new_pvc_info = ppv.pure_gather(new_vvol)

print(new_vvol)
print(new_pvc_info)
