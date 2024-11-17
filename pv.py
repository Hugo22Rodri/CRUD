import click
import sys

# Añadir la ruta del directorio Platzi-Sales al sys.path
sys.path.append('/home/hugo22/Platzi-Sales')

from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE

cli.add_command(clients_commands.all)

if __name__ == '__main__':
    cli()

# import click

# from .clients import commands as clients_commands

# CLIENTS_TABLE = '.clients.csv'

# @click.group()
# @click.pass_context

# def cli(ctx):
#     ctx.obj = {}
#     ctx.obj['clients_table']= CLIENTS_TABLE

# cli.add_command(clients_commands.all)