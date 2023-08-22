import importlib


def test_big_python(mocker):
    mocker.patch("builtins.print")
    importlib.import_module(name="big_python", package="files")

    expected_output = """
    PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
    P   P   Y   Y       T      H    H     O O    N N     N
    P   P    Y Y        T      H    H    O   O   N  N    N
    PPPP      Y         T      HHHHHH    O   O   N   N   N
    P         Y         T      H    H    O   O   N    N  N
    P         Y         T      H    H     O O    N     N N
    P         Y         T      H    H      O     N       N\n"""
    print.assert_called_once_with(expected_output)
