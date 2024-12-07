import click
import sys
from io import StringIO

@click.command()
@click.argument("files", type=click.File(), nargs=-1)
@click.option("-n", is_flag=True, help="Number the lines as they are printed out including blank lines")
@click.option("-b", is_flag=True, help="Number the lines as they are printed out not including blank lines")
def cli(files, n, b):
    file_lines = []
    if len(files) == 0:
        # Convert stdin to a readable file and insert it in one item tuple
        files = (StringIO(sys.stdin.read()),)
    for file in files:
        file_lines.extend(file.readlines())

    count = 1

    for line in file_lines:
        formatted_line = line.split("\n")[0]

        if n:
            click.echo(f"{count} {formatted_line}")
            count += 1
        elif b:
            if formatted_line == '':
                click.echo(formatted_line)
            else:
                click.echo(f"{count} {formatted_line}")
                count += 1
        else:
            click.echo(formatted_line)

if __name__ == "__main__":
    cli()
