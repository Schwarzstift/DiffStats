from data_acquisition.GitDataProvider import GitDataProvider
from visualization import Treemap
from data_acquisition import GroupGenerator
from data_acquisition import ANTLRDataProvider


def show_file_size_in_repo():
    git_data_provider = GitDataProvider(".")
    files_and_sizes = git_data_provider.get_files_with_sizes()
    Treemap.simple_treemap(files_and_sizes)


def show_diff():
    git_data_provider = GitDataProvider(".")
    data = git_data_provider.changes_since("b44e0bd8")
    GroupGenerator.generate_filesystem_groups(data)

    Treemap.colored_grouped_treemap(data)


def show_parsed_size():
    git_data_provider = GitDataProvider(".")
    files_and_sizes = git_data_provider.get_files_with_sizes()

    data = ANTLRDataProvider.parse_files(files_and_sizes.index)
    data = GroupGenerator.generate_cpp_parse_groups(data)
    Treemap.colored_grouped_treemap(data)

if __name__ == '__main__':
    # show_file_size_in_repo()
    # show_diff()
    show_parsed_size()
