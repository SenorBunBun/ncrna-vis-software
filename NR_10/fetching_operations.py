import json
import plotly.express as px

iteration = 'NR_10'

data = json.load(open('{0}.json'.format(iteration)))

def plot_profile(rna_id, protein):
    fig = px.bar(data[rna_id]['pfs'][protein],
                 labels={
                     'value' : 'Strength',
                     'index' : 'Sequence Index'
                 },
                 title="Binding Profile of {0} on RNA {1}".format(protein, rna_id))
    fig.update_traces(marker_color='black')
    fig.show()

#Assuming peaks are inclusive (both the start and ends have peaked values)
def fetch_seq_from_peaks(rna_id):
    peak_dict = data[rna_id]['pks']
    print("Sequences correlating to Peaks for {0} \n".format(rna_id))

    if peak_dict is None:
        print(peak_dict)
    else:
        for protein in peak_dict.keys():
            print("For {0}:".format(protein))
            for inds in peak_dict[protein]:
                print(data[rna_id]['seq'][inds[0]:inds[1] + 1])
            print("")


#plot_profile('NR_038418.1', 'CPSF6')
#fetch_seq_from_peaks('NR_038306.1')
#plot_profile('NR_038444.1', 'CPSF6')
