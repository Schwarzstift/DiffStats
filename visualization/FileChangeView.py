import matplotlib.pyplot as plt
import squarify
import pandas as pd


def file_size_treemap(file_to_line_mapping: pd.DataFrame):
    filtered_mapping = file_to_line_mapping[file_to_line_mapping['size'] > 0]

    squarify.plot(sizes=filtered_mapping['size'], label=filtered_mapping.index, alpha=0.6)
    plt.axis('off')
    plt.show()
