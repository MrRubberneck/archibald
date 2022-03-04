# Archibald, a command line tool for inspecting archimate files

import click
import re
import new_menu

regex_for_checking_file_extension = re.compile(r"\S+.archimate")


def is_correct_extension(file_name):
    return regex_for_checking_file_extension.match(file_name) is not None


def is_correct_contents(file_contents):
    return "<archimate:mode" in file_contents


@click.command()
@click.option("--file", help="Specify the archimate file")
def process_file(file):
    with open(file) as f:
        file_contents = f.read()
    if is_correct_extension(file):
        if is_correct_contents(file_contents):
            new_menu.main()

        else:
            print("Invalid file contents")
    else:
        print("Invalid file extension")


if __name__ == '__main__':
    process_file()
