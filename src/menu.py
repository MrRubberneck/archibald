import cli
import sys
from consolemenu import *
from consolemenu.items import *
from lxml import etree


def main():
    with open(cli.EXP_FILE) as f:
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

        def list_business_services():
            pattern = root.xpath("//element[@* = 'archimate:BusinessService']")
            process_matches(pattern)

        def list_business_roles():
            pattern = root.xpath("//element[@* = 'archimate:BusinessRole']")
            process_matches(pattern)

        def list_by_type():
            """Display all of the "X", where X is any archimate model object"""

            query = input("Pass the object you wish to find(like DiagramObject): \n")
            pattern = root.xpath(f"//element[@* = 'archimate:{query}']")
            if not pattern:
                pattern = root.xpath(f"//child[@* = 'archimate:{query}']")
            process_matches(pattern)

        def show_matched_duplicates():
            """Show all of the matched duplicates. A matched duplicate is one with
            the same object type (business service for example), and identical or
            slightly different (lowercase/uppercase/mixed case, or typo) names."""

            query = input("Enter duplicates to find: ")
            pattern = root.xpath(f"//element[@* = 'archimate:{query}']")

            if not pattern:
                pattern = root.xpath(f"//child[@* = 'archimate:{query}']")

            result = ''
            counter = 0
            for child in pattern:
                result += str(child.attrib)[45:] + '\n---------------------------------\n'
                counter += 1

            declare_duplicates = False
            if counter > 1:
                declare_duplicates = True

            pu = PromptUtils(Screen())

            if declare_duplicates == True:
                pu.println(counter," duplicates have been found")
            else:
                print("No duplicates found")

            pu.enter_to_continue()




        menu = ConsoleMenu(
            "Archibald", "A command line tool for inspecting archimate files."
        )

        business_services = FunctionItem(
            "List Business Services", list_business_services
        )
        business_roles = FunctionItem(
            "List Business Roles", list_business_roles
        )
        by_type = FunctionItem(
            "List by type", list_by_type
        )
        matched_duplicates = FunctionItem(
            "Show matched duplicates - to be implemented", show_matched_duplicates
        )

        menu.append_item(business_services)
        menu.append_item(business_roles)
        menu.append_item(by_type)
        menu.append_item(matched_duplicates)
        menu.show()
