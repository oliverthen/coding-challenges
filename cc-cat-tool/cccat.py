import click
import sys


@click.command()
@click.argument("file", type=click.File())
# @click.option("-c", is_flag=True, help="Count the number of bytes in a file")
def cli(file):
#    if file is None or file == '-':
#     click.echo(file)   
   click.echo(file.read())

if __name__ == "__main__":
    cli()
