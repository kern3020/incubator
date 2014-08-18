from jinja2 import Template
import os

class ConfigBcbio(object):
    def __init__(self):
        # some runs from ERP002442 study
        #                    normal,      cancer
        self.list_of_runs = [('ERR256781', 'normal'), ('ERR256782', 'cancer'),  
                             ('ERR256783', 'normal'), ('ERR256784', 'cancer'), 
                             ('ERR256785', 'normal'), ('ERR256786', 'cancer'), 
                             ('ERR256787', 'normal'), ('ERR256788', 'cancer'),
                             ('ERR256789', 'normal'), ('ERR256790', 'cancer')]

        self.header = '''
# This yaml file was automaticately generated. 
---
details:'''

        self.footer = '''
fc_date: '2014-01-06'
fc_name: cancer
upload:
  dir: ../final
'''

        self.sample = '''
- algorithm:
    aligner: bwa
    coverage_interval: regional
    mark_duplicates: false
    recalibrate: false
    realign: false
    platform: illumina
    quality_format: standard
    variant_regions: ../input/ERP002442-targeted.bed
    variantcaller: freebayes
  analysis: variant2
  description: {{ sample }}
  files:
  - ../input/{{ sample }}_1.fastq.gz
  - ../input/{{ sample }}_2.fastq.gz
  genome_build: GRCh37
  metadata:
    batch: batch1
    phenotype: {{ phenotype }}
'''
        
    def generate_conf(self, data_dir, fname):
        f1 = os.path.join(data_dir, fname)
        with open(f1, "w") as c_file:
            c_file.write(self.header)
            t1 = Template(self.sample)
            for s, p in self.list_of_runs:
                c_file.write(t1.render(sample=s, phenotype=p))
            c_file.write(self.footer)


if __name__ == '__main__': 
    conf = ConfigBcbio()
    conf.generate_conf("/home/jkern/scratch/230", 'cancer-normal.yaml')

