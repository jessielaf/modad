import click
import yaml
from modad.assembler import Assembler
from modad.dissembler import Dissembler
from modad.parser import Parser


@click.group()
def cli():
    """
    Modular assembler and dissembler
    """

    pass


@cli.command()
@click.option("-c", "--config", default="modad.yml", help="The config location")
def assemble(config):
    """
    Assembles modular monolith
    """

    with open(config, "r") as stream:
        Parser(yaml.safe_load(stream))
        Assembler().run()


@cli.command(short_help="Dissembles a module into a destination")
@click.argument("module_name")
@click.argument("dissemble_dest")
@click.option("-c", "--config", default="modad.yml", help="The config location")
def dissemble(module_name, dissemble_dest, config):
    """
    Dissembles the module with MODULE_NAME into the DISSEMBLE_DEST

    MODULE_NAME: The name of the module that will be dissembled
    DISSEMBLE_DEST: The destination in which the module will be dissembled
    """

    with open(config, "r") as stream:
        Parser(yaml.safe_load(stream))
        Dissembler().run(module_name, dissemble_dest)


cli_obj = click.CommandCollection(sources=[cli])


def main():
    cli()
