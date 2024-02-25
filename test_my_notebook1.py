from testbook import testbook
import pandas as pd

# define test function using Testbook for first test using regular data
@testbook('Feature1-Network-Analysis.ipynb', execute=True)
def test_create_graph_regular_data(tb):
    # retrieve the create_graph function from the notebook
    create_graph = tb.ref("create_graph")

    # call create_graph with the test data CSV file path
    test_data_path = "NetworkTestData.csv"
    my_graph = create_graph(test_data_path)

    # perform assertions to test the functionality
    assert len(my_graph.nodes()) == 3

# define test function using Testbook for second test using missing data
@testbook('Feature1-Network-Analysis.ipynb', execute=True)
def test_create_graph_missing_data(tb):
    # retrieve the create_graph function from the notebook
    create_graph = tb.ref("create_graph")

    # call create_graph with the test data CSV file path
    test_data_path = "NetworkMissingTestData.csv"
    my_graph = create_graph(test_data_path)

    # perform assertions to test the functionality
    assert len(my_graph.nodes()) == 3

# define test function using Testbook for third test using duplicated data
@testbook('Feature1-Network-Analysis.ipynb', execute=True)
def test_create_graph_duplicate_data(tb):
    # Retrieve the create_graph function from the notebook
    create_graph = tb.ref("create_graph")

    # Call create_graph with the test data CSV file path
    test_data_path = "NetworkDuplicateTestData.csv"
    my_graph = create_graph(test_data_path)

    # Perform assertions to test the functionality
    assert len(my_graph.nodes()) == 3
