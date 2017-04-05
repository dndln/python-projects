import click

@click.command()
@click.option('--verbose', '-v', is_flag=True, help='Will print verbose messages.')
@click.option('--name', '-n', default='', help='Who are you?')
def cli(verbose, name):
    """This is a sample project to learn Click."""

    if verbose:
        click.echo('We are in verbose mode.')
    click.echo('Hello World')
    click.echo('Bye {0}!'.format(name))
