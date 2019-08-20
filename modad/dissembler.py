import shutil
from os import path
from modad.state import state
from modad.utils import clone, remove_dir


class Dissembler:
    dissemble_dest = ""

    def run(self, module_name, dissemble_dest):
        self.dissemble_dest = dissemble_dest

        if path.exists(self.dissemble_dest):
            remove_dir(self.dissemble_dest)

        module = next(
            module for module in state.config.modules if module.name == module_name
        )
        clone(module, self.dissemble_dest)

        if isinstance(state.config.dest, list):
            self.multiple_destinations(module)
        else:
            self.single_destination(module)

    def single_destination(self, module):
        shutil.move(f"{state.config.dest}/{module.name}", self.dissemble_dest)

    def multiple_destinations(self, module):
        for destination in state.config.dest:
            directory = f"{self.dissemble_dest}/{destination.src}"

            remove_dir(directory)
            shutil.move(f"{destination.dest}/{module.name}", directory)
