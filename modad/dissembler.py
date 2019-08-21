import json
import shutil
from os import path
from modad.config import config
from modad.utils import clone, remove_dir


class Dissembler:
    """
    This class dissembler a certain modules of the modular monolith based on the config

    Attributes;
        dissemble_dest (str): Dissemble destination for the module
        commit_hashes (dict): Commit hashes that are cloned
    """

    dissemble_dest = ""
    commit_hashes = {}

    def run(self, module_name, dissemble_dest):
        """
        Runs the dissembler

        Args:
            module_name: The module that will be dissembled
            dissemble_dest: The destination where the module will be dissembled to
        """

        self.dissemble_dest = dissemble_dest
        with open("modad.lock", "r") as file:
            self.commit_hashes = json.loads(file.read())

        if path.exists(self.dissemble_dest):
            remove_dir(self.dissemble_dest)

        module = next(module for module in config.modules if module.name == module_name)
        clone(module, self.dissemble_dest, self.commit_hashes[module.name])

        if isinstance(config.dest, list):
            self.handle_multiple_destinations(module)
        else:
            self.handle_single_destination(module)

    def handle_single_destination(self, module):
        """
        Runs the dissembler for a single destination

        Args:
            module: The module that will be dissembled
        """

        shutil.move(path.join(config.dest, module.name), self.dissemble_dest)

    def handle_multiple_destinations(self, module):
        """
        Runs the dissembler for multiple destinations

        Args:
            module: The module that will be dissembled
        """

        for destination in config.dest:
            directory = path.join(self.dissemble_dest, destination.src)

            remove_dir(directory)
            shutil.move(path.join(destination.dest, module.name), directory)
