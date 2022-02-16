# CLI for Archibald written in Click

import click
import re


@click.command()
@click.option("--file", help="Specify the archimate file here")
def input_file(file):
    """Accept the file, check if it's the right one"""

    with open(file) as f:
        p = re.compile(r"\S+.archimate")
        if p.match(file) is not None:
            # extension checks are passed
            print("File extension is correct")
        else:
            print("Incorrect file extension")
