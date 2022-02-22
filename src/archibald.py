# Archibald, a command line tool for inspecting archimate files

import click
import re
import menu

regex_for_checking_file_extension = re.compile(r"\S+.archimate")


def is_correct_extension(file_name):
    if regex_for_checking_file_extension.match(file_name) is not None:
        return 'yes'
    else:
        print("Incorrect file extension")
        raise SystemExit()


def is_correct_contents(file_contents):
    if "<archimate:model" in file_contents:
        return 'yes'
    else:
        print("Incorrect file contents ")
        raise SystemExit()


@click.command()
@click.option("--file", help="Specify the archimate file")
def process_file(file):

    with open(file) as file_contents:
        if is_correct_extension(file) == 'yes':
            if is_correct_contents(file_contents.read()) == 'yes':
                menu.main()


if __name__ == '__main__':
    process_file()