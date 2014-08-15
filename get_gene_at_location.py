from __future__ import print_function

import pdb
import os
import time

import mysql.connector
from mysql.connector import errorcode

'''
# this class was inspired by this biostars post. 
# https://www.biostars.org/p/76957/
# but re-written in python

mysql --user=genome --host=genome-mysql.cse.ucsc.edu -A -N -e \
"SELECT kg.chrom, kg.txStart, kg.txEnd, x.geneSymbol \
FROM knownGene kg, kgXref x \
WHERE kg.chrom LIKE '{0}' AND kg.txStart >= {1} AND kg.txEnd < {2} \
GROUP BY(x.geneSymbol) \
LIMIT 10;" hg19
'''

class UcscGenome (object):
    def __init__(self):
        self.config = {
            'user': 'genome',
            'host': 'genome-mysql.cse.ucsc.edu',
            'database': 'hg19',
            'raise_on_warnings': True,
        }
        self.cnx=None
        self.cursor=None

    def __enter__(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
            else:
                print(err)
        else:
            self.cursor = self.cnx.cursor() 
        return self

    def __exit__(self, type, value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.cnx:
            self.cnx.close()

    def get_genes(self, chr, start, end):
        query = '''SELECT kg.chrom, kg.txStart, kg.txEnd, x.geneSymbol \
        FROM knownGene kg, kgXref x \
        WHERE kg.chrom LIKE '{0}' AND kg.txStart >= {1} AND kg.txEnd < {2} \
        GROUP BY(x.geneSymbol);'''.format(chr, start, end)
        self.cursor.execute(query)
        for (chrom, txStart, txEdn, gene_symbol) in self.cursor:
            print ("\t{0}".format(gene_symbol))


class BedFile (object): 
    def __init__(self, file):
        self.bed_file=file

    def parse_and_call(self):
        with UcscGenome() as ucsc:
            with open(self.bed_file) as bd:
                line = True
                while line:
                    line = bd.readline().split('\t')
                    line = [x.strip() for x in line if x.strip()]
                    if line:
                        chr = 'chr' + line[0]
                        start = line[1]
                        end = line[2]
                        print ("chr: {0}, start: {1}, end: {2}".format(chr, start, end))
                        if chr and start and end:
                            ucsc.get_genes(chr, start, end)
                            time.sleep(0.5) # don't slam ucsc


if __name__ == "__main__":
    file="/home/jkern/wip/Hanetal/ERP002442-targeted.bed"
    bd = BedFile(file)
    bd.parse_and_call()
