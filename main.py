# This is a sample Python script.
from generate_output import generate_output
from parse import parse_yml


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    # call the parser
    data = parse_yml('sample.yml')
    generate_output(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

