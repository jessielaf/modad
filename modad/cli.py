import click
import yaml
from modad.assembler import Assembler
from modad.dissembler import Dissembler
from modad.parser import Parser


@click.group()
def cli():
    """
    Create cli group
    """

    pass


@cli.command()
@click.option("-c", "--config", default="modad.yml")
def assemble(config):
    """
    Assembles modular monolith
    """

    with open(config, "r") as stream:
        Parser(yaml.safe_load(stream))
        Assembler().run()


@cli.command()
@click.argument("module_name")
@click.argument("dissemble_dest")
@click.option("-c", "--config", default="modad.yml")
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
