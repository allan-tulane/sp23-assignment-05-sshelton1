from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    visited = set()
    while len(frontier) != 0:
        ###TODO
        current = frontier.pop()
        visited.add(current)
        adjacent = graph[current]
        frontier.update(adjacent)
        frontier.difference_update(visited)
        result.update(adjacent)
    result = sorted(list(result))
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']
    

def connected(graph):
    ### TODO
    n =  len(list(graph.keys()))
    checked = set()
    for node in graph.keys():
        if node not in checked:
            checked.union(graph[node])
            if len(reachable(graph, node)) != n:
                return False
    return True

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    n =  1
    checked = []
    for node in graph.keys():
        if checked == []:
            checked.append(reachable(graph, node))
        else:
            i = 0
            while i < len(checked):
                if node in checked[i]:
                    break
                i += 1
            if i == len(checked):
                checked.append(reachable(graph, node))
            n += 1
    return n

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2
