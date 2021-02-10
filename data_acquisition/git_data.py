from git import Repo
import os


def get_repository(path):
    return Repo(path)


def iterate_over_tree(tree, files):
    for entry in tree.blobs:
        files.append(entry.path)
    for subtree in tree.trees:
        iterate_over_tree(subtree, files)


def get_head_ref(repo: Repo):
    return repo.head.ref


def files_touched_between(repo: Repo, ref_before:str, ref_after:str):
    tree_before = repo.commit(ref_before).tree

    tree_after = repo.commit(ref_after).tree


def get_tracked_files(repo: Repo, ref:str):
    files = []
    tree = repo.commit(ref).tree
    iterate_over_tree(tree, files)
    return files


if __name__ == '__main__':
    path = os.path.join(os.path.curdir, "..")
    get_tracked_files(path)
