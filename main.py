import yaml
from src.assembler import Assembler
from src.parser import Config
from src.state import state

if __name__ == "__main__":
    # todo: make this dynamic with click
    with open("example_config.yml", "r") as stream:
        state.config = Config(yaml.safe_load(stream))
        Assembler().run()
