# write a parser for reading a yml file
# this yml file consists of a list of objects
# each object has a name and a list of attributes
# this parser should return a list of objects as a python dict

import yaml

def parse_yml(file):
    with open(file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def validate_yml(data):
    pass