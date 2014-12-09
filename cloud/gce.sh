#!/bin/bash

HOST=ameba
ZONE=us-central1-a
TYPE=n1-standard-2

if [ "$#" -ne 1 ] 
then
  echo "Usage: gce.sh {ssh | start | stop}"
  exit 1 
fi

CMD="$1"

case ${CMD} 
  in
  "ssh")   gcloud compute ssh ${HOST} ;;
  "start") gcloud compute instances create ${HOST} --zone ${ZONE} --machine-type ${TYPE} ;;
  "stop") gcloud compute instances delete ${HOST} --zone ${ZONE} ;;
  *) echo "unknown command, ${CMD}. Ignoring."
esac
# ssh-keygen -f "~/.ssh/known_hosts" -R 130.211.148.213
