""" We have an array of straight connections between drones. Each connection is represented as a string with two names of
friends separated by hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should write a
function that allow determine more complex connection between drones. You are given two names also. Try to determine if they
are related through common bonds by any depth. For example: if two drones have a common friends or friends who have common
friends and so on.
Let's look at examples:
scout2 and scout3 have the common friend scout1 so they are related. super and scout2 are related
through sscout, scout4 and scout1. But dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.
Output: Are these drones related or not as a boolean.
"""

import pprint
import itertools

def check_connection(network, first, second):

    pairs = [p.split("-") for p in network]

    pp = pprint.PrettyPrinter()
    print("-"*30,"PAIRS","-"*30)
    pp.pprint(pairs)
    print("\n")
    if len(network) > 45:
        print("Network too large")
        return False

    graph = {key: [] for key in list(itertools.chain.from_iterable(pairs))}

    # Build a graph with all the pairs
    for pair in pairs:
         graph[pair[0]].extend([pair[1]])
         graph[pair[1]].extend([pair[0]])

    print("-"*30,"GRAPH","-"*30)
    pp.pprint(graph)

    # now check if 'second' is linked to 'first'
    return find_path(graph,first,second) != None

def find_path(graph, start, end, path=[]):
    print("Start:",start,"; End:",end)
    path = path+[start]
    if start == end:
        return path
    else:
        if not start in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph,node,end,path)
                if newpath:
                    return newpath
        return None


if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
            ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
             "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                            "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
            ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
             "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                            "super", "scout2") == True, "Super Scout"
    assert check_connection(
             ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
              "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                            "dr101", "sscout") == False, "I don't know any scouts."

