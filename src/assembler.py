import shutil
import tempfile
from os import path, makedirs
from src.state import state
from src.utils import remove_dir, clone

TEMP_DIR = tempfile.gettempdir()


class Assembler:
    def run(self):
        try:
            if isinstance(state.config.dest, list):
                self.handle_mapped_destination()
            else:
                self.handle_single_destination()
        finally:
            for directory in state.temp_folders:
                remove_dir(directory)

    def handle_single_destination(self):
        for name, module in state.config.modules.items():
            directory = f"{state.config.copy_dir}/{name}"
            remove_dir(directory)
            clone(module, directory)

    def handle_mapped_destination(self):
        # Create the to-directory if it does not exist
        for destination in state.config.dest:
            if not path.exists(destination.dest):
                makedirs(destination.dest)

        # Clone the modules and copy the right directories
        for module in state.config.modules:
            directory = f"{TEMP_DIR}/{module.name}"
            remove_dir(directory)
            clone(module, directory)

            for destination in state.config.dest:
                to_directory = f"{destination.dest}/{module.name}"
                remove_dir(to_directory)
                shutil.move(f"{TEMP_DIR}/{module.name}/{destination.src}", to_directory)
