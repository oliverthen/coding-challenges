import click


@click.command()
# @click.argument("file", type=click.File(), default=sys.stdin)
# @click.option("-c", is_flag=True, help="Count the number of bytes in a file")
def cli():
   click.echo("Hello")

if __name__ == "__main__":
    cli()
