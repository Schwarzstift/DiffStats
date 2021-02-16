import matplotlib.pyplot as plt
import squarify
import pandas as pd
import plotly.express as px

colors = {'U': 'gray', 'M': 'orange', 'A': 'green', 'D': 'black'}
group_label = "group"
identifier_label = "identifier"
size_label = "size"
change_type_label = "change type"


def simple_treemap(data: pd.DataFrame):
    # Shows a simple treemap as static image. Index is used as name of the items
    assert not data[size_label].empty

    filtered_mapping = data[data[size_label] > 0]

    squarify.plot(sizes=filtered_mapping[size_label],
                  label=filtered_mapping.index,
                  alpha=0.6)
    plt.axis('off')
    plt.show()


def colored_grouped_treemap(data: pd.DataFrame):
    # Shows a colored tree map according to colors
    assert not data[group_label].empty  # Defines in which group the identifiers are
    assert not data[identifier_label].empty  # Defines the displayed names of the identifiers
    assert not data[size_label].empty  # Defines the size within the treemap of each identifier
    assert not data[change_type_label].empty  # Defines the changes to the file see colors definition above

    filtered_mapping = data[data[size_label] > 0]

    fig = px.treemap(filtered_mapping,
                     path=[group_label, identifier_label],
                     values=size_label,
                     color=change_type_label,
                     color_discrete_map=colors
                     )
    fig.show()
