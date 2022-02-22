# CLI for Archibald written in Click

import re
import click
import menu


EXP_FILE = ''

@click.command()
@click.option("--file", help="Specify the archimate file here")

# accept the file
# check if the file extension is correct
# check if contents are correct


def input_file(file):
    """Accept the file, check if it's the right one"""

    with open(file) as f:
        # check file extension and contents for correctness
        global EXP_FILE
        EXP_FILE = file
        ext_reg = re.compile(r"\S+.archimate")
        if ext_reg.match(file) is not None:
            # file extension check passed

            cont_reg = re.compile(r"<archimate:model")
            if cont_reg.findall(f.read()) == ["<archimate:model"]:
                # contents check passed
                menu.main()
            else:
                print("File contents are incorrect.")

        else:
            print("Incorrect file extension")


