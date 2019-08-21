from modad.config import config, Module, Destination


class Parser:
    """
    Parses the config file into the config state

    Attributes:
        unparsed_config (dict): The unparsed config dictionary
    """

    unparsed_config: dict = {}

    def __init__(self, config):
        self.parse_dest(config)
        self.parse_modules(config)

    def parse_modules(self, unparsed_config):
        """
        Parses the modules in the config

        Args:
            unparsed_config: The dictionary from the config file
        """

        modules = unparsed_config.get("modules", None)

        if not modules:
            raise Exception("Modules not in config")

        if not isinstance(modules, list):
            raise Exception("Modules should be a list")

        for module in modules:
            config.modules.append(Module(**module))

    def parse_dest(self, unparsed_config):
        """
        Parses the destination in the config

        Args:
            unparsed_config: The dictionary from the config file
        """

        dest = unparsed_config.get("dest", None)

        if not dest:
            raise Exception("Dest not in config")

        if isinstance(dest, str):
            config.dest = dest
        elif isinstance(dest, list):
            config.dest = []

            for destination in dest:
                config.dest.append(Destination(**destination))
        else:
            raise Exception("Dest should either be a list or a string")
