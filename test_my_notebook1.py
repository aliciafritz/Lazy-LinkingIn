# import packages needed

import testbook

@testbook.test
def test_network_analysis(tb):
    # execute the entire notebook
    tb.execute_notebook("Feature1-Network-Analysis.ipynb", timeout=600)

    # test 1: Check if the number of nodes in the graph is non-zero
    tb.execute_cell("G.number_of_nodes()")
    num_nodes = tb.cell_output()
    assert num_nodes > 0, "Number of nodes is zero"

    # test 2: Check if the number of edges in the graph is non-zero
    tb.execute_cell("G.number_of_edges()")
    num_edges = tb.cell_output()
    assert num_edges > 0, "Number of edges is zero"

    # test network statistics
    tb.execute_cell("print('Number of nodes:', G.number_of_nodes())")
    tb.execute_cell("print('Number of edges:', G.number_of_edges())")
    tb.execute_cell("print('Average degree:', sum(dict(G.degree()).values()) / G.number_of_nodes())")

    # check if network statistics are calculated correctly
    expected_output = "Number of nodes: {}\nNumber of edges: {}\nAverage degree: {}".format(num_nodes, num_edges, (num_edges*2)/num_nodes)
    assert tb.cell_output() == expected_output, "Network statistics calculation failed"
