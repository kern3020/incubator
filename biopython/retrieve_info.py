import os
import sys

from Bio import Entrez

if 'ENTREZ_EMAIL' in os.environ:
    Entrez.email = os.environ['ENTREZ_EMAIL']

def retrieve_info(gene_syms, bed_file, notes_file):
    '''given a list of gene_syms and file handles for output, retrieve the
    location and description. Location information is saved in bed
    format. The description is simply pprinted.
    '''
    for gene in gene_syms:
        search_term = "{0}[gene] AND Homo sapiens[organism]".format(gene)
        hits = []
        handle = Entrez.esearch(db="gene", term=search_term)
        results = Entrez.read(handle)
        for gene_id in results['IdList']:
            handle = Entrez.esummary(db="gene", id=gene_id)
            summary = Entrez.read(handle)
            if summary[0]['Name'] == gene:
                # location
                chromo = summary[0]['Chromosome']
                start = summary[0]['GenomicInfo'][0]['ChrStart']
                stop = summary[0]['GenomicInfo'][0]['ChrStop']
                bed_file.write('{0}\t{1}\t{2}\t{3}\n'.format(chromo, start, stop, gene))

                # descriptions
                desc_short = summary[0]['Description']
                desc_long = summary[0]['Summary']
                notes_file.write('{0}(chr: {1}) - {2}\n'.format(gene, chromo, desc_short))
                notes_file.write('Summary: {0}\n\n'.format(desc_long))
                

if __name__ == "__main__":
    bed = 'genes.bed'
    if os.path.exists(bed):
        os.remove(bed)
    notes = 'notesOnGenes.txt'
    if os.path.exists(notes):
        os.remove(notes)
    with open(bed, 'w+') as bed_file:
        with open(notes, 'w+') as notes_file:
            gene_list = ['APC', 'FBXW7', 'GNAS', 'KRAS', 'MAFB','SRC', 
                         'SMAD4', 'TP53', 'TTN']
            # gene_list = ['APC']
            retrieve_info(gene_list, bed_file, notes_file)
