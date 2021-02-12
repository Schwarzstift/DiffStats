from data_acquisition.GitDataProvider import GitDataProvider
from data_acquisition.FileDataProvider import FileDataProvider
from visualization import FileChangeView

if __name__ == '__main__':
    head_ref = "39a7aa1d"
    before_ref = "2f41b077"
    git_data_provider = GitDataProvider(".")

    list_of_files_head = git_data_provider.get_tracked_files(head_ref)
    map_files_to_num_lines = FileDataProvider.get_lines_from_file(list_of_files_head)

    files_touched_since = git_data_provider.files_touched_between(head_ref, before_ref)

    FileChangeView.file_size_treemap(map_files_to_num_lines)
