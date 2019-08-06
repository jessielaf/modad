import subprocess

from git import Repo


def remove_dir(directory):
    """
    Remove a directory

    Args:
        directory: path that should be removed
    """
    subprocess.check_output(["rm", "-rf", directory])


def clone(module, directory):
    """
    Clones a module to a directory

    Args:
        module: Module that is defined in the config
        directory: Directory to which it should be copied
    """

    repo = Repo.clone_from(module.repo, directory)
    repo.git.checkout(module.version)
