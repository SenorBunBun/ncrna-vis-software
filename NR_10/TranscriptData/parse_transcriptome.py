import re
from Bio import SeqIO
import pandas as pd

table_dict = {
    'accessionID' : [],
    'gene' : [],
    'variant': [],
    'RNA' : [],
    'comments' : []
}

gene_idx = -1
rna_idx = -1
variant_num = -1

for record in SeqIO.parse("transcriptome.fasta", "fasta"):
    parsed_record = re.split(', |; ', record.description)

    table_dict['accessionID'].append(record.id)

    # Both gene_idx and rna_idx are always redefined for this data
    for i in range(len(parsed_record)):
        if parsed_record[i][-1] == ")":
            gene_idx = i
        if gene_idx != -1:
            if parsed_record[i][-3:] == 'RNA':
                rna_idx = i
            if parsed_record[i][-1].isnumeric():
                # Only recording variant number names, not alternative names
                variant_num = parsed_record[i][-1]

    # Finding the gene abbrev.
    table_dict['gene'].append(parsed_record[gene_idx][parsed_record[gene_idx].find("(")+1:parsed_record[gene_idx].find(")")])

    table_dict['RNA'].append(parsed_record[rna_idx])

    # Checking if we defined variant_num, as records can have no variant defined
    table_dict['variant'].append(variant_num if variant_num != -1 else None)

    # Checking if there is parsed data after the RNA, which indicates a comment, verified that if condition is true there is a comment
    table_dict['comments'].append(parsed_record[rna_idx+1] if rna_idx + 1 != len(parsed_record) else None)

transcriptome_df = pd.DataFrame(data=table_dict)
