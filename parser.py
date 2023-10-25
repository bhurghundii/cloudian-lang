import graphviz as gv

from asset_mapper import mapTypeToImage

done = {}


def parse_tokens(data):
    g = gv.Digraph(format='png', graph_attr={"splines": "ortho", "nodesep": "2"})

    # order the group nodes so nodes w/ no deps go first
    for nodes in list(data.items()):
        generate_nodes(data, nodes, g)

    # add edges
    for obj in list(data.items()):
        if obj[1]['type'] != "subnet":
            for input in obj[1]['contain']:
                g.edge(obj[0], input)

    return g


def generate_nodes(data, node, parent):
    if node[1]["type"] == "subnet":
        with parent.subgraph(name="cluster_" + node[0]) as c:
            c.attr(color='black')
            c.attr(rank='same')
            c.attr(labelloc='b')
            c.attr(label=node[0])

            for nodes in node[1]['contain']:
                if done.get(nodes) is None:
                    done[node[0]] = 1
                    generate_nodes(data, [nodes, data[nodes]], c)

    else:
        if done.get(node[0]) is None:
            parent.node(node[0], shape="box", label=node[0], labelloc="b", height="1.3",
                        image=mapTypeToImage(node[1]['type']))
            done[node[0]] = 1
