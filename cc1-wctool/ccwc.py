import click
import os


@click.command()
@click.argument("filename", required=True)
@click.option("-c", is_flag=True, help="Count the number of bytes in a file")
def cli(filename, c):
    if c:
        cur_dir = os.getcwd()
        cur_path = os.path.join(cur_dir, filename)
        num_bytes = os.path.getsize(cur_path)
        click.echo(f"{num_bytes} {filename}")

if __name__ == "__main__":
    cli()
