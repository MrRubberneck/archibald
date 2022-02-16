from consolemenu import *
from consolemenu.items import *
import sys

def displ_dupl():
    pu = PromptUtils(Screen())
    pu.enter_to_continue()

menu = ConsoleMenu("Archibald", "A command line tool for inspecting archimate files")

display_duplicate = FunctionItem("List any duplicate objects in the archimate model", displ_dupl)


if __name__ == '__main__'
menu.append_item(display_duplicate)
menu.show()
