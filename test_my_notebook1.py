from testbook import testbook
import pandas as pd

# define test function using Testbook for first test of regular data
@testbook('Feature1-Network-Analysis.ipynb', execute=True)
def test_create_graph(tb):
    # Retrieve the create_graph function from the notebook
    create_graph = tb.ref("create_graph")

    # Call create_graph with the test data CSV file path
    test_data_path = "/Users/aliciafritz/Desktop/TestData.csv"
    my_graph = create_graph(test_data_path)

    # Perform assertions to test the functionality
    assert len(my_graph.nodes()) == 3

# define test function using Testbook for second test of missing data
@testbook('Feature1-Network-Analysis.ipynb', execute=True)
def test_create_graph(tb):
    # Retrieve the create_graph function from the notebook
    create_graph = tb.ref("create_graph")

    # Call create_graph with the test data CSV file path
    test_data_path = "/Users/aliciafritz/Desktop/MissingTestData.csv"
    my_graph = create_graph(test_data_path)

    # Perform assertions to test the functionality
    assert len(my_graph.nodes()) == 3

# define test function using Testbook for third test of duplicated data
@testbook('Feature1-Network-Analysis.ipynb', execute=True)
def test_create_graph(tb):
    # Retrieve the create_graph function from the notebook
    create_graph = tb.ref("create_graph")

    # Call create_graph with the test data CSV file path
    test_data_path = "/Users/aliciafritz/Desktop/DuplicateTestData.csv"
    my_graph = create_graph(test_data_path)

    # Perform assertions to test the functionality
    assert len(my_graph.nodes()) == 3
