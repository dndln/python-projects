import click
import random

@click.group()
def cli():
    pass

@cli.command()
@click.option('--verbose', '-v', is_flag=True, help='Will print verbose messages.')
@click.option('--name', '-n', default='', help='Who are you?')
def hello(verbose, name):
    """This is a sample project to learn Click."""

    if verbose:
        click.echo('We are in verbose mode.')
    click.echo('Hello World')
    click.echo('Bye {0}!'.format(name))

@cli.command()
@click.option('--num_dice', '-nd', default=1, type=int, help='How many dice you want to roll.')
@click.option('--dice_range', '-dr', default=(1,6), nargs=2, type=int, help='Two ints, lower and upper bound of the dice.')
def roll(num_dice, dice_range):
    """This rolls dice for you."""
    lower_bound = dice_range[0]
    upper_bound = dice_range[1]

    if num_dice == 1:
        click.echo('You are rolling 1 die!')
    else:
        click.echo('You are rolling {} dice!'.format(num_dice))

    click.echo('Your dice go from {} to {}!'.format(lower_bound, upper_bound))

    for roll in range(num_dice):
        roll_result = random.randint(lower_bound, upper_bound)
        print('You rolled {}!'.format(roll_result))
