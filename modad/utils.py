import subprocess

from git import Repo


def remove_dir(directory):
    """
    Remove a directory

    Args:
        directory: path that should be removed
    """
    subprocess.check_output(["rm", "-rf", directory])


def clone(module, directory, commit_hash=None):
    """
    Clones a module to a directory

    Args:
        module: Module that is defined in the config
        directory: Directory to which it should be copied
        commit_hash: Hash of the commit that will be checked out. If this is not passed the version of the module will be used
    """

    repo = Repo.clone_from(module.repo, directory)

    if hash:
        repo.git.checkout(commit_hash)
    else:
        repo.git.checkout(module.version)
