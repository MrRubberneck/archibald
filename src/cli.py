# CLI for Archibald written in Click

import click
import re
from menu import menu


@click.command()
@click.option("--file", help="Specify the archimate file here")
def input_file(file):
    """Accept the file, check if it's the right one"""

    with open(file) as f:
        # check file extension and contents for correctness

        ext_reg = re.compile(r"\S+.archimate")
        if ext_reg.match(file) is not None:
            # file extension check passed

            cont_reg = re.compile(r"<archimate:model")
            if cont_reg.findall(f.read()) == ["<archimate:model"]:
                pass

                # contents check passed
            else:
                print("File contents are incorrect.")

        else:
            print("Incorrect file extension")


@click.option("--menu", help="Launch menu with options to work with the specified file")




