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

college = "yale"
college_color_1 = '#0f4d92'
college_color_2 = 'Black'


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


num_rows = 0
total_polarity = 0
total_subjectivity = 0

polarities = []
subjectivities = []
with open(resource_path(college + "_comments_final.csv"), 'r', encoding="utf8") as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        try:
            sentence = row[1]
            blob = TextBlob(sentence)
            polarities.append(blob.sentiment.polarity)
            subjectivities.append(blob.sentiment.subjectivity)
            num_rows += 1
            total_polarity += blob.sentiment.polarity
            total_subjectivity += blob.sentiment.subjectivity
            # print(blob.word_counts)
            # print(sentence)
            # print(blob.sentiment.polarity, blob.sentiment.subjectivity)
        except:
            # print("This line is blank.")
            pass
print("Average Polarity for " + college.upper() +
      ": " + str(total_polarity/num_rows))
print("Average Subjectivity for " + college.upper() +
      ": " + str(total_subjectivity/num_rows))

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
    marker=dict(
        color=college_color_1,
        size=15,
        line=dict(
            color=college_color_2,
            width=2
        )
    )
    # marker_color=primary_colors[2],
))


fig.update_layout(title=college.upper() + " Sentiment Analysis",
                  xaxis={
                      'title': {'text': 'Subjectivity (0 is objective, 1 is subjective)'}},
                  yaxis={
                      'title': {'text': 'Polarity (-1 is Negative, 0 is Neutral, 1 is Positive)'}},
                  #   legend={'title': {'text': 'Political Party'}},
                  template=theme_hodp)

fig.show()
