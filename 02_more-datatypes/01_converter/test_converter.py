import importlib


def test_converter(mocker):
    mocker.patch("builtins.print")

    importlib.import_module(name="converter", package="files")

    expected_output = ("p", "y", "t", "h", "o", "n", "c", "o", "u", "r", "s", "e")

    print.assert_called_once_with(expected_output)
