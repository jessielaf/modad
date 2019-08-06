import shutil
from modad.state import state
from modad.utils import clone, remove_dir


class Dissembler:
    dissemble_dest = ""

    def run(self, module_name, dissemble_dest):
        self.dissemble_dest = dissemble_dest

        module = next(
            module for module in state.config.modules if module.name == module_name
        )
        clone(module, self.dissemble_dest)

        if isinstance(state.config.dest, list):
            self.multiple_destinations()
        else:
            self.single_destination()

    def single_destination(self):
        shutil.move(state.config.dest, self.dissemble_dest)

    def multiple_destinations(self):
        for destination in state.config.dest:
            directory = f"{self.dissemble_dest}/{destination.src}"

            remove_dir(directory)
            shutil.move(destination.dest, directory)
