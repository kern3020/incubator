

DATA_DIR="~/scratch/230/ERP002442"
cd ${DATA_DIR}
mkdir input config work final

cd input

for SAMPLE in "ERR256781" "ERR256782" "ERR256783" "ERR256784" "ERR256785" \
    "ERR256786" "ERR256787" "ERR256788" "ERR256789" "ERR256790"
do
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR256/${SAMPLE}/${SAMPLE}_1.fastq.gz
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR256/${SAMPLE}/${SAMPLE}_2.fastq.gz
done

