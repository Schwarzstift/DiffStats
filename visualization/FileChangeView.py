import matplotlib.pyplot as plt
import squarify


def file_size_treemap(file_to_line_mapping: dict):
    filtered_mapping = {k: v for k, v in file_to_line_mapping.items() if v > 0}

    squarify.plot(sizes=filtered_mapping.values(), label=filtered_mapping.keys(), alpha=0.6)
    plt.axis('off')
    plt.show()
