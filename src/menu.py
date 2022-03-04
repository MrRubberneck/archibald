import sys
from consolemenu import *
from consolemenu.items import *
from lxml import etree

# read the file in lxml compatible way
# given a pattern
# produce a string with matches
# output the string to menu


def produce_output(pattern):
    result = ''
    counter = 0
    for i in pattern:
        result += str(i.attrib)[45:] + '\n---------------------------------\n'
        counter += 1
    return result


def display_output(result):  # here goes result from produce_output()
    pu = PromptUtils(Screen())
    pu.println(result + '\nNumber of matches: ')
    pu.enter_to_continue()


def list_business_services(root):
    pattern = root.xpath("//element[@* = 'archimate:BusinessService']")
    result = produce_output(pattern)
    display_output(result)


def main():
    with open("../tests/fretardos-pizza.archimate") as file:
        file_contents = file.read()
    root = etree.XML(bytes(file_contents, encoding='utf8'))

    menu = ConsoleMenu("Archibald", "A command line tool for inspecting archimate files.")
    business_services = FunctionItem("List Business Services", list_business_services)

    menu.append_item(business_services)
    menu.show()
