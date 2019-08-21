import json
import shutil
import subprocess
import tempfile
from os import path, makedirs
from modad.config import config
from modad.utils import remove_dir, clone

TEMP_DIR = tempfile.gettempdir()


class Assembler:
    """
    This class assembles the modular monolith based on the config

    Attributes:
        commit_hashes (dict): Commit hashes per module
    """

    commit_hashes = {}

    def run(self):
        """
        Runs the assembler
        """

        if isinstance(config.dest, list):
            self.handle_multiple_destinations()
        else:
            self.handle_single_destination()

        self.create_modad_lock()

    def handle_single_destination(self):
        """
        Runs the assembler for a single destination
        """

        for module in config.modules:
            directory = path.join(config.dest, module.name)
            remove_dir(directory)
            clone(module, directory)
            self.commit_hashes[module.name] = self.get_commit_hash(directory)

    def handle_multiple_destinations(self):
        """
        Runs the assembler for multiple destinations
        """

        # Create the to-directory if it does not exist
        for destination in config.dest:
            if not path.exists(destination.dest):
                makedirs(destination.dest)

        # Clone the modules and copy the right directories
        for module in config.modules:
            directory = path.join(TEMP_DIR, module.name)
            remove_dir(directory)
            clone(module, directory)

            self.commit_hashes[module.name] = self.get_commit_hash(directory)

            for destination in config.dest:
                to_directory = f"{destination.dest}/{module.name}"
                remove_dir(to_directory)
                shutil.move(f"{TEMP_DIR}/{module.name}/{destination.src}", to_directory)

    def get_commit_hash(self, directory):
        """
        Get the commit hash of the repository

        Args:
            directory: The directory in which the module is cloned

        Returns:
            The commit hash
        """

        return (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=directory)
            .decode("utf-8")
            .replace("\n", "")
        )

    def create_modad_lock(self):
        """
        Creates the lock file for modad
        """

        with open("modad.lock", "w") as file:
            file.write(json.dumps(self.commit_hashes))
