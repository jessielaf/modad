import json
import shutil
from os import path
from modad.config import config
from modad.utils import clone, remove_dir


class Logger:
    """
    Logger for the assembler
    """

    @staticmethod
    def dissemble_module(module, commit_hash):
        """
        Logs when dissembling a module

        Args:
            module: Module that is being dissembled
            commit_hash: The commit hash that was used when assembling
        """

        print(f"Dissembling module: {module.name} from commit: f{commit_hash}")


class Dissembler:
    """
    This class dissembler a certain modules of the modular monolith based on the config

    Attributes;
        dissemble_dest (str): Dissemble destination for the module
    """

    dissemble_dest = ""

    def run(self, module_name, dissemble_dest):
        """
        Runs the dissembler

        Args:
            module_name: The module that will be dissembled
            dissemble_dest: The destination where the module will be dissembled to
        """

        self.dissemble_dest = dissemble_dest

        if path.exists(self.dissemble_dest):
            remove_dir(self.dissemble_dest)

        module = next(module for module in config.modules if module.name == module_name)

        with open("modad.lock", "r") as file:
            commit_hash = json.loads(file.read())[module.name]

        Logger.dissemble_module(module, commit_hash)
        clone(module, self.dissemble_dest, commit_hash)

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
