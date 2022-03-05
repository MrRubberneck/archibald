import sys
from consolemenu import *
from consolemenu.items import *
from lxml import etree
import state


def produce_output(pattern):
    """The procedure for matches in the following functions"""
    result = ''
    counter = 0
    for child in pattern:
        result += str(child.attrib)[45:] + '\n---------------------------------\n'
        counter += 1
    return result, counter


def display_output(result, counter):
    pu = PromptUtils(Screen())
    pu.println(result + '\nNumber of matches: ' + str(counter))
    pu.enter_to_continue()


def display_to_user(pattern):
    output, counter = produce_output(pattern)
    display_output(output, counter)


def list_business_services():
    pattern = state.root.xpath("//element[@* = 'archimate:BusinessService']")
    display_to_user(pattern)


def list_business_roles():
    pattern = state.root.xpath("//element[@* = 'archimate:BusinessRole']")
    display_to_user(pattern)


def list_by_type():
    """Display all the "X", where X is any archimate model object"""

    query = input("Pass the object you wish to find(like DiagramObject): \n")
    pattern = state.root.xpath(f"//element[@* = 'archimate:{query}']")
    if not pattern:
        pattern = state.root.xpath(f"//child[@* = 'archimate:{query}']")
    display_to_user(pattern)


def show_matched_duplicates():
    """Show all the matched duplicates. A matched duplicate is one with
    the same object type (business service for example), and identical or
    slightly different (lowercase/uppercase/mixed case, or typo) names."""

    query = input("Enter duplicates to find: ")
    pattern = state.root.xpath(f"//element[@* = 'archimate:{query}']")
    if not pattern:
        pattern = state.root.xpath(f"//child[@* = 'archimate:{query}']")
    _, counter = produce_output(pattern)
    pu = PromptUtils(Screen())
    if counter > 1:
        pu.println(counter," duplicates have been found")
    else:
        print("No duplicates found")
    pu.enter_to_continue()


def main():
    with open(state.file_path) as f:
        file = f.read()
    state.root = etree.XML(bytes(file, encoding='utf8'))

    menu = ConsoleMenu("Archibald", "A command line tool for inspecting archimate files.")
    business_services = FunctionItem("List Business Services", list_business_services)
    business_roles = FunctionItem("List Business Roles", list_business_roles)
    by_type = FunctionItem("List by type", list_by_type )
    matched_duplicates = FunctionItem("Show matched duplicates - to be implemented", show_matched_duplicates)
    menu.append_item(business_services)
    menu.append_item(business_roles)
    menu.append_item(by_type)
    menu.append_item(matched_duplicates)
    menu.show()
