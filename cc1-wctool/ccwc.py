import click
import os
import sys
from io import StringIO, BytesIO


@click.command()
@click.argument("file", type=click.File(), default=sys.stdin)
@click.option("-c", is_flag=True, help="Count the number of bytes in a file")
@click.option("-l", is_flag=True, help="Count the number of lines in a file")
@click.option("-w", is_flag=True, help="Count the number of words in a file")
@click.option("-m", is_flag=True, help="Count the number of chars in a file")
def cli(file, c, l, w, m):
    if file != sys.stdin:
        file_name = file.name
        std_input = False
    else:
        file_name = ''
        std_input = True
        file = StringIO(file.read())

    if c:
        num_bytes = count_bytes(file, std_input)
        click.echo(f"{num_bytes} {file_name}")
    elif l:
        num_lines = count_lines(file)
        click.echo(f"{num_lines} {file_name}")
    elif w:
        num_words = count_words(file)
        click.echo(f"{num_words} {file_name}")
    elif m:
        num_chars = count_chars(file, std_input)
        click.echo(f"{num_chars} {file_name}")
    else:
        num_lines = count_lines(file)
        num_words = count_words(file)
        num_bytes = count_bytes(file, std_input)

        click.echo(f"{num_lines} {num_words} {num_bytes} {file_name}")


def count_bytes(file, std_input):
    if not std_input:
        file.seek(0, os.SEEK_END)
        return file.tell()
    else:
        # Need to convert StringIO buffer to BytesIO Buffer to count bytes
        data = file.getvalue()
        byte_data = data.encode('utf-8')
        buffer = BytesIO(byte_data)
        return len(buffer.read())


def count_lines(file):
    file.seek(0)
    file_lines = file.readlines()
    num_lines = 0
    for line in file_lines:
        num_lines += 1
    return num_lines


def count_words(file):
    file.seek(0)
    file_lines = file.readlines()
    num_words = 0
    for line in file_lines:
        split_words = line.split()
        num_words += len(split_words)
    return num_words


def count_chars(file, std_input):
    file.seek(0)
    if not std_input:
        data = file.read()
        # Need to add count of lines as above line for regular file does not count newline char
        return len(data) + count_lines(file)
    else:
        data = file.read()
        return len(data)


if __name__ == "__main__":
    cli()
