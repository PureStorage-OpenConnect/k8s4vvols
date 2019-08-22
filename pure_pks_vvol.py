from kubernetes import client, config
import purestorage as ps

# Never do this in prod. SSL warnings are there for a reason. but for a demo, they are the worst.
import urllib3
urllib3.disable_warnings()

#Use your fa IP and Token Here
fa_ip = "<FlashArray IP>"
fa_api_token = "<FlashArray User API Token>"

def k8s_gather(pvc_name):
    config.load_kube_config(config_file="<Path to KUBECONFIG")
    v1 = client.CoreV1Api()
    pvc_array = v1.list_persistent_volume_claim_for_all_namespaces(field_selector="metadata.name=" + pvc_name, watch=False)
    for i in pvc_array.items:
        pv_name = i.spec.volume_name
    pv_array = v1.list_persistent_volume(field_selector="metadata.name=" + pv_name, watch=False)
    for i in pv_array.items:
        vmw_path = i.spec.vsphere_volume.volume_path
    x = vmw_path.find('/') +1
    vmw_path_clean = vmw_path[x:]
    vmw_out = vmw_path_clean
    pv_out = pv_name
    return pv_out, vmw_out, pvc_array, pv_array

def pure_gather(vmw_in):
    array = ps.FlashArray(fa_ip, api_token=fa_api_token)
    get_info = array.list_volumes(tags=True)
    get_info_str = str(get_info)
    temp_str = get_info_str.replace('"', "")
    temp_list = temp_str.split('}')
    match_list = [s for s in temp_list if vmw_in in s]
    temp_name = match_list
    temp_name = str(temp_name[0])
    list_name = temp_name.split(",")
    list_name = list_name[2].strip("'name': ")
    vvol_name = list_name
    return vvol_name

def pure_snap(vol_name):
    array = ps.FlashArray(fa_ip, api_token=fa_api_token)
    make_snap = array.create_snapshot(vol_name)
    temp_name = make_snap
    temp_name = str(temp_name)
    list_name = temp_name.split(",")
    list_name = list_name[3].strip("'name': ")
    make_snap = list_name
    return make_snap

def list_snap(vol_name):
    array = ps.FlashArray(fa_ip, api_token=fa_api_token)
    get_snap = array.get_volume(vol_name, snap=True)
    return get_snap

def pure_new_vol(snap_name, dest_name):
    array = ps.FlashArray(fa_ip, api_token=fa_api_token)
    new_vol = array.copy_volume(snap_name, dest_name)
    return new_vol

def pure_vol_info():
    array = ps.FlashArray(fa_ip, api_token=fa_api_token)
    get_info = array.list_volumes(tags=True)
    get_info_str = str(get_info)
    temp_str = get_info_str.replace('"', "")
    temp_list = temp_str.split('}')
    print(temp_list)
    match_list = [s for s in temp_list if vol_name in s]
    temp_name = match_list
    temp_name = str(temp_name)
    list_name = temp_name.split(",")
    list_name = get_info_str
    return list_name
