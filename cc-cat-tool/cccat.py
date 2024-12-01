import click


@click.command()
@click.argument("files", type=click.File(), nargs=-1)
@click.option("-n", is_flag=True, help="Number the lines as they are printed out")
def cli(files, n):   
   for file in files:
    file_lines = file.readlines()
       
    for count, line in enumerate(file_lines, 1):
       # Remove new line character
       formatted_line = line.split("\n")[0]

       if not n:
        click.echo(formatted_line)
        continue 

       click.echo(f"{count} {formatted_line}")

if __name__ == "__main__":
    cli()
