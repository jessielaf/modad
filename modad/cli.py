import click
import yaml
from modad.assembler import Assembler
from modad.dissembler import Dissembler
from modad.parser import Config
from modad.state import state


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


def main():
    cli()
