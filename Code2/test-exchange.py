import nose.tools as n
import exchange


def test_open_file():
    f = "../data/usd_cad.csv"
    actual = exchange.open_file(f)
    n.assert_equal(type(actual), list, 'Incorrect import.  Please import as list.')

def test_clean_data():
    data = exchange.open_file("../data/usd_cad.csv")
    actual = exchange.clean_data(data)
    n.assert_not_equal(len(actual), len(data), "Data is not fully cleaned")

def test_calculate_diffs():
    data = exchange.open_file("../data/usd_cad.csv")
    clean_data = exchange.clean_data(data)
    actual = exchange.calculate_diffs(clean_data)
    n.assert_almost_equals(actual[0][1], 0.0001, places=9)


def test_pretty_output():
    data = exchange.open_file("../data/usd_cad.csv")
    clean_data = exchange.clean_data(data)
    diffs = exchange.calculate_diffs(clean_data)
    output = exchange.pretty_output(diffs)
    n.assert_equal(len(output), 121, 'String requires formatting')
