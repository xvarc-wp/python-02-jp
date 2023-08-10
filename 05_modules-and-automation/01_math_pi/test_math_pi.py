import importlib


def test_math_pi(mocker):
    mocker.patch("builtins.print")
    importlib.import_module(name="math_pi", package="files")

    expected_output = 3.141592653589793

    print.assert_called_once_with(expected_output)
