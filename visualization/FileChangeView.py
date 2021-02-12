import matplotlib.pyplot as plt
import squarify
import pandas as pd
import plotly.express as px

colors = {'U': 'gray', 'M': 'orange', 'A': 'green', 'D': 'black'}


def file_size_treemap(file_to_line_mapping: pd.DataFrame):
    filtered_mapping = file_to_line_mapping[file_to_line_mapping['size'] > 0]

    squarify.plot(sizes=filtered_mapping['size'],
                  label=filtered_mapping.index,
                  alpha=0.6)
    plt.axis('off')
    plt.show()


def updated_file_size_treemap(data: pd.DataFrame):
    filtered_mapping = data[data['size'] > 0]
    filtered_mapping = filtered_mapping.replace({"change type": colors})

    squarify.plot(sizes=filtered_mapping['size'],
                  label=filtered_mapping.index,
                  alpha=0.6,
                  color=filtered_mapping['change type'])
    plt.axis('off')
    plt.show()


def updated_file_size_treemap_v2(data: pd.DataFrame):
    filtered_mapping = data[data['size'] > 0]
    filtered_mapping = filtered_mapping.replace({"change type": colors})

    fig = px.treemap(filtered_mapping,
                     path=['group', 'identifier'],
                     values='size',
                     color='change type'
                     )
    fig.show()

