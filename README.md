# K8s4vvols
List, Snap and Clone vvols used for Kubernetes Persistent Volumes

## Start with PyVmomi
I started here with the great examples written for python and first class disks.

[PyVomi Community Examples](https://github.com/vmware/pyvmomi-community-samples/tree/master/samples)

## Other required packages

We need the kubernetes module and the purestorage module for python.

```bash
pip install kubernetes
pip install purestorage
```
If you are using macosx and it is messing up your python environment you might need to:

```bash
pip3 install kubernetes
pip3 install purestorage
```
It is also required to have **Ansible 2.8.x** installed.

## How to use to import to PKS functions

1. First add your FlashArray IP and API token in two places.

```bash
pure_pks_vvol.py
and
clone-play.yml
```

  Each should have a clearly marked section for you to edit.
Also edit the pure_pks_vvol.py file and change this line to match your KUBECONFIG. Failure to do so will result in more failing.

  ```
  config.load_kube_config(config_file="<Path to KUBECONFIG>")
  ```

2. Run the shell script (or create your own), you must supply the source PVC name or it will fail.

This script will scale down the deployment, in this demo script it is minio-deployment in the PKS cluster named testcluster. Your environment will vary. Please edit the script. Know the risks of messing with deployments and only do this if you are sure you have this right. I would hate for you to take down a Production app because you were playing with my script. Also, If you skip this section and do it anyway. It isn't my fault.

Also we assume you are using PSO. Make the pso-

```
./k8s2pks.sh <Your PVC Name>
```


## FCD python files
These are for reference, mostly. The ansible playbook and python do not call them directly but might use the "tools" folder these scrips use. Honestly, these are handy to have around.
