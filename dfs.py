from stack import Stack
from puzzle import Puzzle

try:
    import pydot_ng as pydot
except ImportError:
    import pydot

s = Stack()
explored = []


def dfs(initial_state):
    graph = pydot.Dot(graph_type='digraph', label="8 Puzzle State Space ("
                                                  "DFS) \n Aashish Dhakal \n "
                                                  "CE 4th Year \n Roll: 11",
                      fontsize="30", color="red",
                      fontcolor="black", style="filled", fillcolor="black")
    start_node = Puzzle(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()
    s = Stack()
    s.push(start_node)
    explored = []
    print("The starting node is \ndepth=%d\n" % start_node.depth)
    print(start_node.display())
    while not (s.isEmpty()):
        node = s.pop()
        print("the node selected to expand is\n")
        print("depth=%d\n" % node.depth)
        print(node.display())
        explored.append(node.state)
        graph.add_node(node.graph_node)
        if node.parent:
            graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node,
                                      label=str(node.action)))
        if node.depth < 5:
            children = node.generate_child()
            print("the children nodes of this node are\n")
            for child in children:
                if child.state not in explored:
                    print("depth=%d\n" % child.depth)
                    print(child.display())
                    if child.goal_test():
                        print("This is the goal state")
                        graph.add_node(child.graph_node)
                        graph.add_edge(pydot.Edge(child.parent.graph_node,
                                                  child.graph_node,
                                                  label=str(child.action)))
                        draw_legend(graph)
                        graph.write_png('solution.png')
                        return child.find_solution()
                    s.push(child)
        else:
            print(
                "the depth has exceeded its limit, so we don't expand this node.\n")
    return


def draw_legend(graph):
    graphlegend = pydot.Cluster(graph_name="legend", label="Legend",
                                fontsize="20", color="red",
                                fontcolor="black", style="filled",
                                fillcolor="white")

    legend1 = pydot.Node('Processed node', shape="plaintext")
    graphlegend.add_node(legend1)
    legend2 = pydot.Node("Depth limit reached", shape="plaintext")
    graphlegend.add_node(legend2)
    legend3 = pydot.Node('Goal Node', shape="plaintext")
    graphlegend.add_node(legend3)

    node1 = pydot.Node("1", style="filled", fillcolor="coral", label="")
    graphlegend.add_node(node1)
    node2 = pydot.Node("2", style="filled", fillcolor="springgreen", label="")
    graphlegend.add_node(node2)
    node3 = pydot.Node("3", style="filled", fillcolor="aquamarine2", label="")
    graphlegend.add_node(node3)

    graph.add_subgraph(graphlegend)
    graph.add_edge(pydot.Edge(legend1, legend2, style="invis"))
    graph.add_edge(pydot.Edge(legend2, legend3, style="invis"))

    graph.add_edge(pydot.Edge(node1, node2, style="invis"))
    graph.add_edge(pydot.Edge(node2, node3, style="invis"))
