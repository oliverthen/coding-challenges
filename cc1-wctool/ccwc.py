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
        num_bytes = count_bytes(filename)
        click.echo(f"{num_bytes} {filename}")
    elif l:
        num_lines = count_lines(filename)
        click.echo(f"{num_lines} {filename}")
    elif w:
        num_words = count_words(filename)
        click.echo(f"{num_words} {filename}")
    elif m:
        num_chars = count_chars(filename)
        click.echo(f"{num_chars} {filename}")
    else:
        num_bytes = count_bytes(filename)
        num_lines = count_lines(filename)
        num_words = count_words(filename)
        click.echo(f"{num_lines} {num_words} {num_bytes} {filename}")

def count_bytes(filename):
    cur_dir = os.getcwd()
    cur_path = os.path.join(cur_dir, filename)
    return os.path.getsize(cur_path)

def count_lines(filename):
    with open(filename) as file:
        num_lines = 0
        for line in file:
            num_lines += 1
    return num_lines

def count_words(filename): 
    with open(filename) as file:
        num_words = 0
        for line in file:
            split_words = line.split()
            num_words += len(split_words)
    return num_words

def count_chars(filename):
    with open(filename) as file:
        num_chars = 0
        for line in file:
            for char in line:
                num_chars += 1
            # Account for new line character
            num_chars += 1
    return num_chars

if __name__ == "__main__":
    cli()
