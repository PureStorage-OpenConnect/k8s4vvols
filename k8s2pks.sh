#!/bin/bash
##
# Written by Jon Owings
# GitHub: https://github.com/2vcps
# Email: owings@purestorage.com
# Website: http://blog.2vcps.io
#
# Note: Example code For testing purposes only
#
# This code has been released under the terms of the Apache-2.0 license
# http://opensource.org/licenses/Apache-2.0
##############
#Make sure to scale the destination so we don't corrupt the volume

kubectl scale deployment minio-deployment --replicas=0 --context=testcluster

#setup to get the source volume from the PVC name

#This is set when PSO is installed. Make this match your PSO namespace
pso_ns='k8s-'
#The the pv name from k8s
source_pv=`kubectl get pvc --context=lab01|grep $1 |head |awk '{print $3}'`

#Python script using pure python SDK, Kubernetes module, and pyvmomi this maps the pvc to the vVol
vvol=`python3 get_vvol_from_pvc.py -p $1`

#combing the strings and run the ansilbe playbook, followed up my bring the app back online.
source_vol=$pso_ns$source_pv
ansible-playbook clone-play.yml --extra-vars "vvol=$vvol source_vol=$source_vol"
kubectl scale deployment minio-deployment --replicas=1 --context=testcluster
kubectl get deployment minio-deployment --context=testcluster

