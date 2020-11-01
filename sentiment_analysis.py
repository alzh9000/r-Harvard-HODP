import sys
import os
from textblob import TextBlob
import csv
import nltk
import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
nltk.download('punkt')


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


polarities = []
subjectivities = []
with open(resource_path("test_text.csv"), 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        try:
            sentence = row[0]
            blob = TextBlob(sentence)
            polarities.append(blob.sentiment.polarity)
            subjectivities.append(blob.sentiment.subjectivity)
            print(blob.word_counts)
            print(sentence)
            print(blob.sentiment.polarity, blob.sentiment.subjectivity)
        except:
            print("This line is blank.")


# colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title={'font': {'size': 24, 'family': "Helvetica",
                        'color': monochrome_colors[0]}, 'pad': {'t': 100, 'r': 0, 'b': 0, 'l': 0}},
        font={'size': 18, 'family': 'Helvetica', 'color': '#717171'},
        xaxis={'ticks': "outside",
               'tickfont': {'size': 14, 'family': "Helvetica"},
               'showticksuffix': 'all',
               'showtickprefix': 'last',
               'showline': True,
               'linewidth': 5,
               'title': {'font': {'size': 18, 'family': 'Helvetica'}, 'standoff': 20},
               'automargin': True
               },
        yaxis={'ticks': "outside",
               'tickfont': {'size': 14, 'family': "Helvetica"},
               'showticksuffix': 'all',
               'showtickprefix': 'last',
               'title': {'font': {'size': 18, 'family': 'Helvetica'}, 'standoff': 20},
               'showline': True,
               'linewidth': 5,
               'automargin': True
               },
        legend={'bgcolor': 'rgba(0,0,0,0)',
                'title': {'font': {'size': 18, 'family': "Helvetica", 'color': monochrome_colors[0]}},
                'font': {'size': 14, 'family': "Helvetica"},
                'yanchor': 'bottom'
                },
        colorscale={'diverging': monochrome_colors},
        coloraxis={'autocolorscale': True,
                   'cauto': True,
                   'colorbar': {'tickfont': {'size': 14, 'family': 'Helvetica'}, 'title': {'font': {'size': 18, 'family': 'Helvetica'}}},
                   }
    )
)

# fig = px.scatter(x=polarities, y=subjectivities)
# fig.show()


fig = go.Figure()


fig.add_trace(go.Scatter(
    x=subjectivities,
    y=polarities,
    mode='markers',
    marker_color=primary_colors[2],
))
# fig.add_trace(go.Scatter(
#     x=rep_df['year'],
#     y=rep_df['candidatevotes'],
#     name='republican',
#     mode='lines+markers',
#     marker_color=primary_colors[0],
# ))
# fig.add_trace(go.Scatter(
#     x=other_df['year'],
#     y=other_df['candidatevotes'],
#     name='others',
#     mode='lines+markers',
#     marker_color=primary_colors[1],
# ))


fig.update_layout(title="Sentiment Analysis",
                  xaxis={
                      'title': {'text': 'Subjectivity (0 is objective, 1 is subjective)'}},
                  yaxis={
                      'title': {'text': 'Polarity (Negative vs. Neutral vs. Positive'}},
                  #   legend={'title': {'text': 'Political Party'}},
                  template=theme_hodp)

fig.show()
