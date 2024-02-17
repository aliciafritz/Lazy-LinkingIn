# import packages needed

from testbook import testbook

@testbook("/Users/aliciafritz/Desktop/Lazy-LinkingIn/Feature1-Network-Analysis.ipynb", execute=True)
def test_network_analysis(tb):
    # check if the number of nodes in the graph is non-zero
    num_nodes = tb.execute_cell("G.number_of_nodes()").result
    assert num_nodes > 0, "Number of nodes is zero"

    # check if the number of edges in the graph is non-zero
    num_edges = tb.execute_cell("G.number_of_edges()").result
    assert num_edges > 0, "Number of edges is zero"

    # check network statistics
    tb.execute_cell("print('Number of nodes:', G.number_of_nodes())")
    tb.execute_cell("print('Number of edges:', G.number_of_edges())")
    tb.execute_cell("print('Average degree:', sum(dict(G.degree()).values()) / G.number_of_nodes())")

    # get the output of the above cells
    num_nodes_output = tb.cell_output()
    num_edges_output = tb.cell_output()
    avg_degree_output = tb.cell_output()

    # check if network statistics are calculated correctly
    expected_output = "Number of nodes: {}\nNumber of edges: {}\nAverage degree: {}".format(num_nodes, num_edges, (num_edges*2)/num_nodes)
    assert num_nodes_output.strip() == expected_output.split('\n')[0], "Number of nodes calculation failed"
    assert num_edges_output.strip() == expected_output.split('\n')[1], "Number of edges calculation failed"
    assert avg_degree_output.strip() == expected_output.split('\n')[2], "Average degree calculation failed"
