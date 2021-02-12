from git import Repo


class GitDataProvider:

    def __init__(self, path):
        self.repo = Repo(path)
        self.current_commit = self.repo.head.commit

    def set_commit(self, rev: str):
        self.current_commit = self.repo.commit(rev)

    def get_all_blobs(self):
        blobs = []
        tree = self.current_commit.tree
        GitDataProvider.__collect_files_in_repository(tree, blobs)
        return blobs

    def get_files_with_sizes(self):
        blobs = self.get_all_blobs()
        return {blob.name: blob.size for blob in blobs}


    @staticmethod
    def __collect_files_in_repository(tree, blobs):
        for entry in tree.blobs:
            blobs.append(entry)
        for subtree in tree.trees:
            GitDataProvider.__collect_files_in_repository(subtree, blobs)

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

    def files_touched_between(self, ref_before: str, ref_after: str):
        tree_before = self.repo.commit(ref_before).tree
        tree_after = self.repo.commit(ref_after).tree
        changed_files = []
        new_files = []
        GitDataProvider.__compare_two_trees(tree_before, tree_after, changed_files, new_files)
        return (changed_files, new_files)
