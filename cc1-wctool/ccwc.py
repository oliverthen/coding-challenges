import click
import os


@click.command()
@click.argument("filename", required=True)
@click.option("-c", is_flag=True, help="Count the number of bytes in a file")
@click.option("-l", is_flag=True, help="Count the number of lines in a file")
@click.option("-w", is_flag=True, help="Count the number of words in a file")
@click.option("-m", is_flag=True, help="Count the number of chars in a file")
def cli(filename, c, l, w, m):
    if c:
        cur_dir = os.getcwd()
        cur_path = os.path.join(cur_dir, filename)
        num_bytes = os.path.getsize(cur_path)
        click.echo(f"{num_bytes} {filename}")
    elif l:
        with open(filename) as file:
            num_lines = 0
            for line in file:
                num_lines += 1
        click.echo(f"{num_lines} {filename}")
    elif w:
        with open(filename) as file:
            num_words = 0
            for line in file:
                split_words = line.split()
                num_words += len(split_words)
        click.echo(f"{num_words} {filename}")
    elif m:
        with open(filename) as file:
            num_chars = 0
            for line in file:
                for char in line:
                    num_chars += 1
                # Account for new line character
                num_chars += 1

        click.echo(f"{num_chars} {filename}")

if __name__ == "__main__":
    cli()
