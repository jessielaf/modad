import click
import yaml
from src.assembler import Assembler
from src.dissembler import Dissembler
from src.parser import Config
from src.state import state


@click.group()
def cli():
    pass


@cli.command()
@click.option("--config", default="modad.yml")
def assemble(config):
    """
    Assembles modular monolith
    """

    with open(config, "r") as stream:
        state.config = Config(yaml.safe_load(stream))
        Assembler().run()


@cli.command()
@click.argument("module_name")
@click.argument("dissemble_dest")
@click.option("--config", default="modad.yml")
def dissemble(module_name, dissemble_dest, config):
    """
    Dissembles modular monolith
    """
    with open(config, "r") as stream:
        state.config = Config(yaml.safe_load(stream))
        Dissembler().run(module_name, dissemble_dest)


cli_obj = click.CommandCollection(sources=[cli])


if __name__ == "__main__":
    cli()
