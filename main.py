from data_acquisition import git_data, file_data
from visualization import tree_map

if __name__ == '__main__':
    list_of_files = git_data.get_tracked_files(".")
    print(list_of_files)
    map = file_data.get_lines_from_file(list_of_files)
    tree_map.file_size_treemap(map)
