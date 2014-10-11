INST=elasticluster-7a7712f2-bf76-4efc-901c-5b6c051f22d4

gcloud compute instances attach-disk ${INST} --disk bcbio --zone us-central1-a
gcloud compute instances attach-disk ${INST} --disk data --zone us-central1-a
