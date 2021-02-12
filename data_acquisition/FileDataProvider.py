

class FileDataProvider:

    @staticmethod
    def get_lines_from_file(list_of_files):
        files_to_num_lines_mapping = {}
        for filename in list_of_files:
            file = open(filename, "r")
            nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
            line_count = len(nonempty_lines)
            if line_count>0:
                files_to_num_lines_mapping[filename] = line_count
        return files_to_num_lines_mapping
