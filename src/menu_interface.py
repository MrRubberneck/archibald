import cli
import sys
from consolemenu import *
from consolemenu.items import *
from lxml import etree


def main():
    with open(cli.exp_file) as f:
        file = f.read()
        root = etree.XML(bytes(file, encoding='utf8'))

        def process_matches(pattern):
            """The procedure for matches in the following functions"""


            result = ''
            counter = 0
            for child in pattern:
                result += str(child.attrib)[45:] + '\n---------------------------------\n'
                counter += 1
            pu = PromptUtils(Screen())
            pu.println(result + '\nNumber of matches: ', counter)
            pu.enter_to_continue()

        def display_business_services():
            pattern = root.xpath("//element[@* = 'archimate:BusinessService']")
            process_matches(pattern)

        def display_business_roles():
            pattern = root.xpath("//element[@* = 'archimate:BusinessRole']")
            process_matches(pattern)

        def show_x_object():
            """Display all of the "X", where X is any archimate model object"""
            query = input("Pass the object you wish to find(like DiagramObject): ")
            pattern = root.xpath(f"//child[@* = 'archimate:{query}']")
            process_matches(pattern)

        menu = ConsoleMenu(
            "Archibald", "A command line tool for inspecting archimate files."
        )

        business_services = FunctionItem(
            "Display Business Services", display_business_services
        )
        business_roles = FunctionItem(
            "Show Business Roles", display_business_roles
        )
        x_object = FunctionItem(
            "Enter an object to find", show_x_object
        )

        menu.append_item(business_services)
        menu.append_item(business_roles)
        menu.append_item(x_object)
        menu.show()
