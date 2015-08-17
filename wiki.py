
__author__ = 'cihankoseoglu'

## A little python program that can help you check wikipedia from your command line interface.

import click
import wikipedia

@click.command()
@click.option('--summary', help= "Gets you the summary for the page you're looking for.")



def mainProgram(summary):
    i = wikipedia.summary(summary)
    click.echo(i)


if __name__ == '__main__':
    mainProgram()
