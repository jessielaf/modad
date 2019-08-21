import shutil
from os import path
from modad.state import state
from modad.utils import clone, remove_dir


class Dissembler:
    """
    This class dissembler a certain modules of the modular monolith based on the config
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

        module = next(
            module for module in state.config.modules if module.name == module_name
        )
        clone(module, self.dissemble_dest)

        if isinstance(state.config.dest, list):
            self.handle_multiple_destinations(module)
        else:
            self.handle_single_destination(module)

    def handle_single_destination(self, module):
        """
        Runs the dissembler for a single destination

        Args:
            module: The module that will be dissembled
        """

        shutil.move(f"{state.config.dest}/{module.name}", self.dissemble_dest)

    def handle_multiple_destinations(self, module):
        """
        Runs the dissembler for multiple destinations

        Args:
            module: The module that will be dissembled
        """

        for destination in state.config.dest:
            directory = f"{self.dissemble_dest}/{destination.src}"

            remove_dir(directory)
            shutil.move(f"{destination.dest}/{module.name}", directory)
