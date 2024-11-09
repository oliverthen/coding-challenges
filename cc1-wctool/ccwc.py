import click

@click.command()
@click.option('--c', help='Count the number of bytes in a file')
@click.argument('file')
def hello():
    click.echo("Hello World")

if __name__ == "__main__":
    hello()