import importlib
import io
import sys

expected_output = """left
straight ahead
straight ahead
DEAD END
right
straight ahead
DEAD END
right
straight ahead
EXIT!!"""


def test_exit_the_conditional_maze(mocker):
    with mocker.patch("sys.stdout", new_callable=io.StringIO):
        importlib.import_module(name="exit_the_conditional_maze", package="files")

        assert sys.stdout.getvalue().strip() == expected_output
