import shutil
import tempfile
from os import path, makedirs
from modad.config import config
from modad.utils import remove_dir, clone

TEMP_DIR = tempfile.gettempdir()


class Assembler:
    """
    This class assembles the modular monolith based on the config
    """

    def run(self):
        """
        Runs the assembler
        """

        if isinstance(config.dest, list):
            self.handle_multiple_destinations()
        else:
            self.handle_single_destination()

    def handle_single_destination(self):
        """
        Runs the assembler for a single destination
        """

        for module in config.modules:
            directory = f"{config.dest}/{module.name}"
            remove_dir(directory)
            clone(module, directory)

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
            directory = f"{TEMP_DIR}/{module.name}"
            remove_dir(directory)
            clone(module, directory)

            for destination in config.dest:
                to_directory = f"{destination.dest}/{module.name}"
                remove_dir(to_directory)
                shutil.move(f"{TEMP_DIR}/{module.name}/{destination.src}", to_directory)
