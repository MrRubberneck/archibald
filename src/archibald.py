# Archibald, a command line tool for inspecting archimate files

import click
import re
import menu

FILE = ''

regex_for_checking_file_extension = re.compile(r"\S+.archimate")
regex_for_checking_file_contents = re.compile(r"<archimate:model")


def is_correct_extension(file_name):
    if regex_for_checking_file_extension.match(file_name) is not None:
        return 'yes'
    else:
        print("Incorrect file extension")
        raise SystemExit()


def is_correct_contents(file_contents):
    if regex_for_checking_file_contents.findall(file_contents) is not None:
        return 'yes'
    else:
        print("Incorrect file contents ")
        raise SystemExit()


@click.command()
@click.option("--file", help="Specify the archimate file")
def process_file(file):
    global FILE
    FILE = file
    with open(file) as f:
        if is_correct_extension(file) == 'yes':
            if is_correct_contents(f.read()) == 'yes':
                menu.main()


if __name__ == '__main__':
    process_file()