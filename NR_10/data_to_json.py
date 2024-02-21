from Bio import SeqIO
import json
import re


iteration = "NR_10"

rna_data = {}

pfiles = open("refseq_{0}_rbp_profile.txt".format(iteration), "r")
peaks = open("refseq_{0}_rbp_peaks.txt".format(iteration), "r")

# Writing profiles to dictionary
# Found profiles linked to 'empty' as their protein
for pfile in pfiles:
    temp_lt = pfile.split()
    if temp_lt[0] not in rna_data:
        rna_data[temp_lt[0]] = {
            'seq' : None,
            'pfs' : {},
            'pks' :  None,
            'md' : None
        }
    # Verified all profiles for RNA has same length and that this stores the entire profile
    rna_data[temp_lt[0]]['pfs'][temp_lt[1]] = list(map(float, temp_lt[2:]))

pfiles.close()

#Writing peak locations to dictionary
missing_ids = []
for line in peaks:
    temp_lt = line.split()

    if temp_lt[0] not in rna_data:
        rna_data[temp_lt[0]] = {
            'seq': None,
            'pfs': {},
            'pks': None,
            'md': None
        }
        missing_ids.append(temp_lt[0])

    if temp_lt[1] != 'None':
        rna_data[temp_lt[0]]['pks'] = {}
        for i in range(1, len(temp_lt)):
            temp_str = re.split(r':|-', temp_lt[i])

            if temp_str[0] not in rna_data[temp_lt[0]]['pks']:
                rna_data[temp_lt[0]]['pks'][temp_str[0]] = []
            rna_data[temp_lt[0]]['pks'][temp_str[0]].append((int(temp_str[1]), int(temp_str[2])))
print("These are id's that were present in the peaks file, but not in the profile file", missing_ids)

#Writing sequences and mtadata to dictionary
missing_ids = []
for record in SeqIO.parse("refseq_{0}.fasta".format(iteration), "fasta"):
    if record.id not in rna_data:
        rna_data[temp_lt[0]] = {
            'seq': None,
            'pfs': {},
            'pks': None,
            'md': None
        }
        missing_ids.append(temp_lt[0])
    rna_data[record.id]['seq'] = str(record.seq)
    rna_data[record.id]['md'] = record.description

print("These are id's that were present in the fasta file, but not in the profile/peaks file", missing_ids)

with open('{0}.json'.format(iteration), 'w') as f:
    json.dump(rna_data, f)
print("RNA data parsed into json at {0}.json".format(iteration))