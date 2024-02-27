
from testbook import testbook
import pandas as pd

# define test function using Testbook for duplicate data and should return 2 instead of 3
@testbook('Feature2-ConnectionGrowth.ipynb', execute=True)
def test_create_graph_regular_data(tb):
    # retrieve the create_graph function from the notebook
    create_graph = tb.ref("connections_growth_graph")

    # call create_graph with the test data CSV file path
    test_data_path = "ConnectionsDateWrong.csv"
    my_graph = create_graph(test_data_path)

    # perform assertions to test the functionality
    print (my_graph)   
    assert len (my_graph.values) == 2  
    
# define test function using Testbook for first test using regular data
@testbook('Feature2-ConnectionGrowth.ipynb', execute=True)
def test_create_graph_regular_data(tb):
    # retrieve the create_graph function from the notebook
    create_graph = tb.ref("connections_growth_graph")

    # call create_graph with the test data CSV file path
    test_data_path = "ConnectionsTest.csv"
    my_graph = create_graph(test_data_path)

    # perform assertions to test the functionality
    print (my_graph)   
    assert len (my_graph.values) == 3  
    
# define test function using Testbook for absense of data
@testbook('Feature2-ConnectionGrowth.ipynb', execute=True)
def test_create_graph_regular_data(tb):
    # retrieve the create_graph function from the notebook
    create_graph = tb.ref("connections_growth_graph")

    # call create_graph with the test data CSV file path
    test_data_path = "ConnectionsDateZero.csv"
    my_graph = create_graph(test_data_path)

    # perform assertions to test the functionality
    print (my_graph)   
    assert len (my_graph.values) == 0      