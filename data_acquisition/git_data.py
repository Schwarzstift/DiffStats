from git import Repo
import os


def iterate_over_tree(tree, files):
    for entry in tree.blobs:
        files.append(entry.path)
    for subtree in tree.trees:
        iterate_over_tree(subtree, files)


def get_tracked_files(path):
    repo = Repo(path)
    files = []

    tree = repo.head.commit.tree
    iterate_over_tree(tree, files)

    return files


if __name__ == '__main__':
    path = os.path.join(os.path.curdir, "..")
    get_tracked_files(path)
