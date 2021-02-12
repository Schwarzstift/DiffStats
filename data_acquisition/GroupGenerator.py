

def split_path_from_filename(complete_path: str):
    return complete_path.rsplit("/", 1)[0]


def split_filename_from_path(complete_path: str):
    return complete_path.rsplit("/", 1)[-1]
