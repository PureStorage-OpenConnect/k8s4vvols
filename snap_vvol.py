from kubernetes import client, config
import purestorage as ps
import pure_pks_vvol as ppv

# Never do this in prod. SSL warning are there for a reason.
import urllib3
urllib3.disable_warnings()

pvc_name = input("Enter PVC Name: ")


pv_name, vmw_path, pvc_array, pv_array = ppv.k8s_gather(pvc_name)
vvolx = ppv.pure_gather(vmw_path)
ah_snap = ppv.pure_snap(vvolx)

print('The persistent volume claim you supplied is:')
print(pvc_name)
print('It maps to this Persistent Volume')
print(pv_name)
print('Which corresponds to this vSphere Path or VMDK')
print(vmw_path)
print('That maps to this VVOL on the FlashArray')
print(vvolx)
print('And the snap is now')
print(ah_snap)

