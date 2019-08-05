from typing import Union, List

from dataclasses import dataclass


@dataclass
class Destination:
    src: str
    dest: str


@dataclass
class Module:
    name: str
    repo: str
    version: str = "master"


class Config:
    dest: Union[str, List[Destination]]
    modules: List[Module] = []

    def __init__(self, config):
        self.parse_dest(config)
        self.parse_modules(config)

    def parse_modules(self, config):
        modules = config.get("modules", None)

        if not modules:
            raise Exception("Modules not in config")

        if not isinstance(modules, list):
            raise Exception("Modules should be a list")

        for module in modules:
            self.modules.append(Module(**module))

    def parse_dest(self, config):
        dest = config.get("dest", None)

        if not dest:
            raise Exception("Dest not in config")

        if isinstance(dest, str):
            self.dest = dest
        elif isinstance(dest, list):
            self.dest = []

            for destination in dest:
                self.dest.append(Destination(**destination))
        else:
            raise Exception("Dest should either be a list or a string")
