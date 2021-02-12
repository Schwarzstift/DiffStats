from data_acquisition.GitDataProvider import GitDataProvider
from visualization import FileChangeView


def show_file_size_in_repo():
    git_data_provider = GitDataProvider(".")
    files_and_sizes = git_data_provider.get_files_with_sizes()
    print(files_and_sizes)
    FileChangeView.file_size_treemap(files_and_sizes)


if __name__ == '__main__':
    show_file_size_in_repo()

    #files_touched_since = git_data_provider.files_touched_between(head_ref, before_ref)

    #FileChangeView.file_size_treemap(map_files_to_num_lines)
