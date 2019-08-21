from typing import Union, List

from dataclasses import dataclass


@dataclass
class Destination:
    """
    Destination when using multiple destinations

    Args:
        src (str): The source of the destination inside the module
        dest: (str): The destination of the module inside the project
    """

    src: str
    dest: str


@dataclass
class Module:
    """

    Args:
        name (str): The name of the module
        repo (str): Repository where the module is located
        version (str): Version of the repository that should be cloned. Defaults to `master`
    """

    name: str
    repo: str
    version: str = "master"


class _Config:
    """
    The config of modad
    """

    dest: Union[str, List[Destination]]
    modules: List[Module] = []


config = _Config()
