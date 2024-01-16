import json
import re

iteration = "gencode_v44"

peaks_mapped = open("{0}_SPIDRv1_peaks_mapped_v1.txt".format(iteration), "r")
next(peaks_mapped)

genome_data = {}

for id in peaks_mapped:
    templt = id.split()
    peaks = templt[5:]
    parsed_peaks = peaks

    if len(peaks) > 1:
        parsed_peaks = []

        for i in peaks:
            split_i = re.split(r':|-', i)
            if len(split_i) != 4:
                print("Error in parsing peaks for {0}".format(templt[0]))
            parsed_peaks.append([split_i[0], (int(split_i[1]), int(split_i[2])), float(split_i[3])])

    genome_data[templt[0]] = {
        "pks" : parsed_peaks,
        "md" : templt[:5]
    }

with open('{0}.json'.format(iteration), 'w') as f:
    json.dump(genome_data, f)
