import click
import sys


@click.command()
@click.argument("files", type=click.File(), nargs=-1)
# @click.option("-c", is_flag=True, help="Count the number of bytes in a file")
def cli(files):
   for file in files:
    click.echo(file.read())

if __name__ == "__main__":
    cli()
