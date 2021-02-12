from git import Repo


class GitDataProvider:

    def __init__(self, path):
        self.repo = Repo(path)

    @staticmethod
    def __collect_files_in_repository(tree, files):
        for entry in tree.blobs:
            files.append(entry.path)
        for subtree in tree.trees:
            GitDataProvider.__collect_files_in_repository(subtree, files)

    @staticmethod
    def __compare_two_trees(tree_before, tree_after, changedFiles, newFiles):
        for blob_after in tree_after.blobs:
            if blob_after not in tree_before.blobs:  # otherwise it has not changed since then
                # Either it is new, renamed or has changed
                # TODO renamed files are considered currently as new files
                if blob_after.path in [b.path for b in tree_before.blobs]:  # has changed?
                    changedFiles.append(blob_after.path)  # same path but different hash -> changed
                else:
                    newFiles.append(blob_after.path)
        for subtree_after in tree_after.trees:
            if subtree_after not in tree_before.trees:  # otherwise it has not changed since then
                # find corresponding tree
                subtree_before = ""
                for subtree in tree_before.trees:
                    if subtree_after.path is subtree.path:
                        subtree_before = subtree
                        break

                if subtree_before != "":
                    GitDataProvider.__compare_two_trees(subtree_before, subtree_after, changedFiles, newFiles)
                else:
                    GitDataProvider.__collect_files_in_repository(subtree_after, newFiles)

    def get_head_ref(self):
        return self.repo.head.ref

    def files_touched_between(self, ref_before: str, ref_after: str):
        tree_before = self.repo.commit(ref_before).tree
        tree_after = self.repo.commit(ref_after).tree
        changed_files = []
        new_files = []
        GitDataProvider.__compare_two_trees(tree_before, tree_after, changed_files, new_files)
        return (changed_files, new_files)

    def get_tracked_files(self, ref: str):
        files = []
        tree = self.repo.commit(ref).tree
        GitDataProvider.__collect_files_in_repository(tree, files)
        return files
