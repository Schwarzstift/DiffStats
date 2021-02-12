from data_acquisition.GitDataProvider import GitDataProvider
from visualization import FileChangeView


def show_file_size_in_repo():
    git_data_provider = GitDataProvider(".")
    files_and_sizes = git_data_provider.get_files_with_sizes()
    FileChangeView.file_size_treemap(files_and_sizes)


def show_diff():
    git_data_provider = GitDataProvider(".")
    paths_and_sizes = git_data_provider.get_files_with_sizes()
    changes = git_data_provider.changes_since("b44e0bd8")

    data = paths_and_sizes.join(changes, how="outer")
    data["size"] = data["size"].fillna(0)
    data["change type"] = data["change type"].fillna("U")

    FileChangeView.updated_file_size_treemap(data)


if __name__ == '__main__':
    # show_file_size_in_repo()
    show_diff()
