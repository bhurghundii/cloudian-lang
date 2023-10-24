# This is a sample Python script.
from generate_output import generate_output
from parse import parse_yml, parse_cloudian, cldn_to_yaml
import yaml

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    lines = parse_cloudian('sample.cldn')
    yamlFile = cldn_to_yaml(lines)

    generate_output(yamlFile)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

