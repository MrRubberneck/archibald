import cli
import sys
from consolemenu import *
from consolemenu.items import *
from lxml import etree


def main():
    with open(cli.exp_file) as f:
        file = f.read()
        root = etree.XML(bytes(file, encoding='utf8'))
        def displ_dupl():
            # display duplicate entries

            pu = PromptUtils(Screen())

            pu.enter_to_continue()

        def displ_bus_serv():
            pattern = root.xpath("//element[@* = 'archimate:BusinessService']")

            result = ''
            for child in pattern:
                result += str(child.attrib) + '\n'
            pu = PromptUtils(Screen())
            pu.println(result)
            pu.enter_to_continue()

        menu = ConsoleMenu(
            "Archibald", "A command line tool for inspecting archimate files."
        )

        display_duplicate = FunctionItem(
            "List any duplicates", displ_dupl
        )
        business_services = FunctionItem(
            "Display Business Services", displ_bus_serv
        )

        menu.append_item(business_services)
        menu.append_item(display_duplicate)
        menu.show()
