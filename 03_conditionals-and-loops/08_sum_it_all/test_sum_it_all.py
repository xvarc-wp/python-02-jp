import importlib
import io
import sys


def test_sum_it_all(mocker):
    with mocker.patch("sys.stdout", new_callable=io.StringIO):
        importlib.import_module(name="sum_it_all", package="files")

        expected_output = "合計: 5050"

        assert sys.stdout.getvalue().strip() == expected_output
