import pandas as pd
from visualization import Treemap


def generate_filesystem_groups(data: pd.DataFrame):
    data[Treemap.group_label] = data.index
    data[Treemap.group_label] = data[Treemap.group_label].apply(_split_path_from_filename)
    data[Treemap.identifier_label] = data.index
    data[Treemap.identifier_label] = data[Treemap.identifier_label].apply(_split_filename_from_path)


def _split_path_from_filename(complete_path: str):
    return complete_path.rsplit("/", 1)[0]


def _split_filename_from_path(complete_path: str):
    return complete_path.rsplit("/", 1)[-1]


def generate_cpp_parse_groups(data: pd.DataFrame):
    data= data.rename(
        columns={"class": Treemap.group_label, "function": Treemap.identifier_label, "size": Treemap.size_label})
    data[Treemap.change_type_label] = "U" #TODO remove this when implemented
    return data
