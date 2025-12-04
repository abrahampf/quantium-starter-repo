from app import app

def test_001_graph_present(dash_duo):
    # start the app
    dash_duo.start_server(app)

    # wait until the graph element is in the DOM
    dash_duo.wait_for_element("#pink_morsels_sales_graph", timeout=10)

    # assert that the element exists
    graph = dash_duo.find_element("#pink_morsels_sales_graph")
    assert graph is not None

def test_002_radio_present(dash_duo):
    # start the app
    dash_duo.start_server(app)

    # wait until the radio element is in the DOM
    dash_duo.wait_for_element("#region_radio", timeout=10)

    # assert that the element exists
    radio = dash_duo.find_element("#region_radio")
    assert radio is not None

def test_003_header_present(dash_duo):
    # start the app
    dash_duo.start_server(app)

    # wait until the header element is in the DOM
    dash_duo.wait_for_element("#graph_title", timeout=10)

    # assert that the element exists
    header = dash_duo.find_element("#graph_title")
    assert header is not None