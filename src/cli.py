# CLI for Archibald written in Click

import click
import re
import menu_interface

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
                # contents check passed
                menu_interface.main()
            else:
                print("File contents are incorrect.")

        else:
            print("Incorrect file extension")




