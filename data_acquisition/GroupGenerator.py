import pandas as pd


def generate_filesystem_groups(data: pd.DataFrame):
    data["group"] = data.index
    data["group"] = data["group"].apply(_split_path_from_filename)
    data["identifier"] = data.index
    data["identifier"] = data["identifier"].apply(_split_filename_from_path)


def _split_path_from_filename(complete_path: str):
    return complete_path.rsplit("/", 1)[0]


def _split_filename_from_path(complete_path: str):
    return complete_path.rsplit("/", 1)[-1]
