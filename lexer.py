def read_cloudian_source(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]

    return lines


def lexer(lines):
    tokens = {}

    for line in lines:
        if "#" in line:
            continue
        elif '=>' in line and '::' in line:
            tokens[line.split('::')[0].strip()] = {"type": line.split('::')[1].split("=>")[0].strip(), "contain": []}
            tokens[line.split('::')[0].strip()]["contain"] = [x.strip() for x in
                                                              line.split('=>')[1].strip()[1:-1].split(',')]

        elif '::' in line:
            tokens[line.split('::')[0].strip()] = {"type": line.split('::')[1].strip(), "contain": []}

        elif '=>' in line:
            tokens[line.split('=>')[0].strip()]["contain"] = [x.strip() for x in
                                                              line.split('=>')[1].strip()[1:-1].split(',')]

    return tokens
