import importlib

import pytest


@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (
            "1,2,3,4,5,6,7,8,9,10",
            "2,4,6,8,10,9,7,5,3,1",
        ),
        (
            "10,1,9,2,8,3,7,4,6,5",
            "1,2,3,4,5,6,7,8,9,10",
        ),
    ],
)
def test_reorder_numbers(mocker, inputs, expected_output):
    mocker.patch("builtins.input", lambda: inputs)
    mocker.patch("builtins.print")

    importlib.reload(
        importlib.import_module(name="reorder_numbers", package="files"),
    )

    print.assert_called_once_with(expected_output)
