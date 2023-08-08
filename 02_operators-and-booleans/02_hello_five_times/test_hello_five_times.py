import importlib


def test_hello_five_times(mocker):
    mocker.patch("builtins.print")
    importlib.import_module(name="hello_five_times", package="files")

    expected_output = "Hello World!Hello World!Hello World!Hello World!Hello World!"
    print.assert_called_once_with(expected_output)
