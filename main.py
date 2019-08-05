import tempfile
import yaml
from git import Repo
from os import makedirs, path
import subprocess
import shutil


TEMP_DIR = tempfile.gettempdir()


class Monoc:
    config = {}
    modules = {}
    copy_dir = ""
    temp_dir = []

    def __init__(self, file_path):
        """
        Args:
            file_path: The path where the yaml is located
        """

        with open(file_path, "r") as stream:
            self.config = yaml.safe_load(stream)
            self.modules = self.config.get("modules", {})
            self.copy_dir = self.config.get("dest_dir", "")

    def run(self):
        """
        Runs monoc
        """

        try:
            # If the copy dir is a dictionary it means that certain folders should be copied to the right folder
            if isinstance(self.copy_dir, dict):
                # Create the to-directory if it does not exist
                for from_dir, to_dir in self.copy_dir.items():
                    if not path.exists(to_dir):
                        makedirs(to_dir)

                # Clone the modules and copy the right directories
                for name, module in self.modules.items():
                    directory = f"{TEMP_DIR}/{name}"
                    self.remove_dir(directory)
                    self.clone(module, directory)

                    for from_dir, to_dir in self.copy_dir.items():
                        to_directory = f"{to_dir}/{name}"
                        self.remove_dir(to_directory)
                        shutil.move(f"{TEMP_DIR}/{name}/{from_dir}", to_directory)
            else:
                # Copy the whole git repo into a folder
                for name, module in self.modules.items():
                    directory = f"{self.copy_dir}/{name}"
                    self.remove_dir(directory)
                    self.clone(module, directory)
        finally:
            self.remove_dirs()

    def clone(self, module, directory):
        """
        Clones a module to a directory

        Args:
            module: Module that is defined in the config
            directory: Directory to which it should be copied
        """

        repo = Repo.clone_from(module["repo"], directory)
        repo.git.checkout(module.get("version", "master"))

    def remove_dirs(self):
        """
        Remove all unused directories
        """

        for directory in self.temp_dir:
            self.remove_dir(directory)

    def remove_dir(self, directory):
        """
        Remove a directory

        Args:
            directory: path that should be removed
        """
        subprocess.check_output(["rm", "-rf", directory])


if __name__ == "__main__":
    # todo: make this dynamic with click
    monoc = Monoc("example_config.yml")
    monoc.run()
