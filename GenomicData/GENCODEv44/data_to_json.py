import json
import re
from Bio import SeqIO

iteration = "gencode_v44"

peaks_mapped = open("{0}_SPIDRv1_peaks_mapped_v1.txt".format(iteration), "r")
next(peaks_mapped)

genome_data = {}

for id in peaks_mapped:
    templt = id.split()
    peaks = templt[5:]
    parsed_peaks = peaks

    if len(peaks) >= 1 and peaks[0] != 'None':
        parsed_peaks = []
        for i in peaks:
            split_i = re.split(r':|-', i)
            if len(split_i) != 4:
                print("Error in parsing peaks for {0}".format(templt[0]))
            parsed_peaks.append([split_i[0], (int(split_i[1]), int(split_i[2])), float(split_i[3])])

    genome_data[templt[0]] = {
        "pks" : parsed_peaks,
        "md" : templt[:5],
        "l" : None
    }

for record in SeqIO.parse("{0}.transcripts.fa".format("gencode.v44"), "fasta"):
    id = record.id.split("|")[0]
    if id not in genome_data:
        print("Error processing sequence data from fasta for {0}".format(id))
    genome_data[id]["l"] = len(record.seq)

with open('{0}.json'.format(iteration), 'w') as f:
    json.dump(genome_data, f)
