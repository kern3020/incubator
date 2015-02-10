#!/bin/bash

HOST=yeast
IMAGE=alga # ubuntu-14-04
TYPE=n1-standard-1
ZONE=us-central1-a

if [ "$#" -lt 1 ] 
then
  echo "Usage: gce.sh {add-disk | ssh | start | stop}"
  exit 1 
fi

CMD="$1"

if [ ${CMD}x = "add-disk"x ] 
then 
  if [ "$#" -eq 3 ]
  then
    DISK_NAME="$2"
    DISK_SIZE="$3"
  else
    echo "Usage: gce.sh add-disk <name> <size>"
    echo "\t size is in gigabytes and must be a mulitple of 10."
    exit 1
  fi
fi

case ${CMD} 
  in
  "add-disk") 
    gcloud compute disks create ${DISK_NAME} --size ${DISK_SIZE}GB --zone ${ZONE} 
    ;; 
  "ssh")   
    gcloud compute ssh ${HOST} --zone ${ZONE} 
    ;;
  "start")
    if [ ${CMD}x = "start"x ] 
    then 
      if [ "$#" -eq 1 ]
      then
        gcloud compute instances create ${HOST} --zone ${ZONE} \
	    --machine-type ${TYPE} --image=${IMAGE}
      else
        gcloud compute instances create ${HOST} --zone ${ZONE} \
            --machine-type ${TYPE} --disk "name=${2}" --image=${IMAGE}
      fi
    fi 

    ;;
  "stop") 
    gcloud compute instances delete ${HOST} --zone ${ZONE} # --keep-disks boot
    ;;
  *) echo "unknown command, ${CMD}. Ignoring."
esac
# ssh-keygen -f "~/.ssh/known_hosts" -R 130.211.148.213
# gcloud compute images create alga --source-disk ameba --source-disk-zone us-central1-a
