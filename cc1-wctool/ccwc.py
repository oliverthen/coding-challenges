import click
import os


@click.command()
@click.argument("file", type=click.File())
@click.option("-c", is_flag=True, help="Count the number of bytes in a file")
@click.option("-l", is_flag=True, help="Count the number of lines in a file")
@click.option("-w", is_flag=True, help="Count the number of words in a file")
@click.option("-m", is_flag=True, help="Count the number of chars in a file")
def cli(file, c, l, w, m):        
    if c:
        num_bytes = count_bytes(file)
        click.echo(f"{num_bytes} {file.name}")
    elif l:
        num_lines = count_lines(file)
        click.echo(f"{num_lines} {file.name}")
    elif w:
        num_words = count_words(file)
        click.echo(f"{num_words} {file.name}")
    elif m:
        num_chars = count_chars(file)
        click.echo(f"{num_chars} {file.name}")
    else:
        num_bytes = count_bytes(file)
        num_lines = count_lines(file)
        num_words = count_words(file)
        click.echo(f"{num_lines} {num_words} {num_bytes} {file.name}")


def count_bytes(file):
    # cur_dir = os.getcwd()
    # cur_path = os.path.join(cur_dir, file)
    # return os.path.getsize(cur_path)
    file.seek(0, os.SEEK_END)
    return file.tell()


def count_lines(file):
    file_lines = file.readlines()
    num_lines = 0
    for line in file_lines:
        num_lines += 1
    return num_lines


def count_words(file):
    file_lines = file.readlines()
    num_words = 0
    for line in file_lines:
        split_words = line.split()
        num_words += len(split_words)
    return num_words


def count_chars(file):
    file_lines = file.readlines()
    num_chars = 0
    for line in file_lines:
        for char in line:
            num_chars += 1
        # Account for new line character
        num_chars += 1
    return num_chars


if __name__ == "__main__":
    cli()
