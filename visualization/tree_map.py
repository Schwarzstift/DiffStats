import matplotlib.pyplot as plt
import squarify
import pandas as pd



def file_size_treemap(file_to_line_mapping):
    sizes = file_to_line_mapping.values()
    labels = file_to_line_mapping.keys()

    squarify.plot(sizes=sizes, label=labels, alpha=0.6)
    plt.axis('off')
    plt.show()
