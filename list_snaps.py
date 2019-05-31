from kubernetes import client, config
import purestorage as ps
import pure_pks_vvol as ppv
# Never do this in prod. SSL warning are there for a reason.
import urllib3
urllib3.disable_warnings()

pvc_name = "redis-master-claim-vvols"
#pvc_name = input("Enter PVC Name: ")
#pvc_name = "redis-master-claim-vvols"

pv_name, vmw_path, pvc_array, pv_array = ppv.k8s_gather(pvc_name)
vvolx = ppv.pure_gather(vmw_path)
my_snaps = ppv.list_snap(vvolx)
print(my_snaps)
