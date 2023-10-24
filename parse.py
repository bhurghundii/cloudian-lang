# write a parser for reading a yml file
# this yml file consists of a list of objects
# each object has a name and a list of attributes
# this parser should return a list of objects as a python dict

import yaml

def parse_yml(file):
    with open(file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def parse_cloudian(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]

    return lines

def cldn_to_yaml(lines):

    # create an empty yaml constructor
    yaml = {}

    # there are 2 rules
    # x::X
    # x => []

    for line in lines:
        if "#" in line:
            continue
        elif '::' in line:
            yaml[line.split('::')[0].strip()] = {"type": line.split('::')[1].strip(), "contain": []}

        elif '=>' in line:
            yaml[line.split('=>')[0].strip()]["contain"] = [x.strip() for x in line.split('=>')[1].strip()[1:-1].split(',')]

    return yaml

def validate_yml(data):
    pass