import json
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

iteration = 'gencode_v44'

data = json.load(open('{0}.json'.format(iteration)))

def plot_cum_RBP_profile(id):
    peaks = data[id]['pks']
    if peaks[0] == 'None':
        print("No peaks found")
        return
    ids = []
    strengths = []
    seqidx = []
    for p in peaks:
        if len(p) != 3:
            print("Error processing {0} and peak {1}".format(id, p))

        count = p[1][1] - p[1][0] + 1
        ids.extend([p[0]]*count)
        strengths.extend([p[2]]*count)
        seqidx.extend(list(range(p[1][0], p[1][1]+1)))

    df = pd.DataFrame(data={'id': ids, 'strength': strengths, 'seqidx': seqidx})
    fig = px.bar(df, x='seqidx', y='strength', color='id', title='RBP Profile for {0}'.format(id), range_x=[0, data[id]['l']])
    fig.update_layout(bargap=0, )
    fig.update_xaxes(range=[0, data[id]['l']])
    fig.show()

def plot_multi_RBP_profiles(id):
    peaks = data[id]['pks']
    if peaks[0] == 'None':
        print("No peaks found")
        return

    titles = []
    for p in peaks:
        titles.append("{0} Binding Profile for {1}".format(p[0], id))

    fig = make_subplots(rows=len(peaks), cols=1, subplot_titles=titles, vertical_spacing=0.05)

    row = 1
    for p in peaks:
        strengths = []
        seqidx = []
        if len(p) != 3:
            print("Error processing {0} and peak {1}".format(id, p))

        count = p[1][1] - p[1][0] + 1
        strengths.extend([p[2]] * count)
        seqidx.extend(list(range(p[1][0], p[1][1] + 1)))

        fig.add_trace(go.Bar(x=seqidx, y=strengths), row=row, col=1, )
        row += 1

    fig.update_layout(height=2000, bargap=0, bargroupgap=0, title_text='RBP Profiles for {0}'.format(id))
    fig.update_xaxes(title_text='Sequence Index', range=[0, data[id]['l']])
    fig.update_yaxes(title_text='Strength')
    fig.show()

plot_multi_RBP_profiles("ENST00000378714.8")


#fig = px.bar(x=[0, 1, 2, 3, 4, 5], y=[0, 1, 1, 1, 0, 0], title='RBP Profile for {0}'.format(id))
#fig.update_layout(bargap=0)
#fig.show()

#np.random.seed=4321
#fig=go.Figure(go.Bar(x=list(range(150)), y=np.random.normal(0,1,150)))
#fig.update_layout(width=600, height=400, bargap=0)
#fig.show()

#np.random.seed=4321
#fig=go.Figure(go.Histogram(x=np.random.normal(0,1,150), histnorm="probability", nbinsx=12))
#fig.update_layout(width=600, height=400, bargap=0)
#fig.show()
