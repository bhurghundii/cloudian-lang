# this file takes a python dict and generates a diagram using graphviz
# the dict is a list objects which contain input, out and a type
# objects are identified by the collection name at the top
# in the inputs, objects are linked together by the name of the object

import graphviz as gv

from asset_mapper import mapTypeToImage

g = gv.Digraph(format='png', graph_attr={"splines": "ortho", "nodesep": "2"})

done = {}

def generate_output(data):

    # order the group nodes so nodes w/ no deps go first
    for nodes in list(data.items()):
        generate_nodes(data, nodes, g)

    # add edges
    for obj in list(data.items()):
        if obj[1]['type'] != "subnet":
            for input in obj[1]['goes_to']:
                g.edge(input, obj[0])

    # render graph
    g.render('output.gv', view=True)

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
        # regular unmarked node
        if (done.get(node[0]) == None):
            parent.node(node[0], shape="box", label=node[0], labelloc="b", height="1.3", image=mapTypeToImage(node[1]['type']))
            done[node[0]] = 1