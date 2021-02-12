from git import Repo
import pandas as pd


class GitDataProvider:

    def __init__(self, path):
        self.repo = Repo(path)
        self.current_commit = self.repo.head.commit

    def set_commit(self, rev: str):
        self.current_commit = self.repo.commit(rev)

    def get_files_with_sizes(self):
        blobs = self.__get_all_blobs()
        blob_info = {blob.path: blob.size for blob in blobs}
        return pd.DataFrame.from_dict(blob_info,
                                      orient='index',
                                      columns=['size'])

    def changes_since(self, rev: str):
        compared_commit = self.repo.commit(rev)
        diff = compared_commit.diff(self.current_commit)
        diff_info = {d.a_path: d.change_type for d in diff}
        data = pd.DataFrame.from_dict(diff_info,
                                      orient='index',
                                      columns=['change type'])
        data = data.join(self.get_files_with_sizes(), how="outer")
        data["size"] = data["size"].fillna(0)
        data["change type"] = data["change type"].fillna("U")
        return data

    def __get_all_blobs(self):
        blobs = []
        tree = self.current_commit.tree
        GitDataProvider.__collect_files_in_repository(tree, blobs)
        return blobs

    @staticmethod
    def __collect_files_in_repository(tree, blobs):
        for entry in tree.blobs:
            blobs.append(entry)
        for subtree in tree.trees:
            GitDataProvider.__collect_files_in_repository(subtree, blobs)
