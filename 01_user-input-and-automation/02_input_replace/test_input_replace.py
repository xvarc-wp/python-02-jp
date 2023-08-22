import importlib

import pytest


class TestInputReplace:
    def _mock_input_factory(self, string, letter):
        """returns mock_input

        It returns a function that mocks builtins.input.
        It should return the different value based on how many times it has been invoked

        - 1st -> returns a variable 'string'
        - 2nd -> returns a variable 'letter'
        - 3rd+ -> returns empty string (edge case)
        """

        call = 0

        def mock_input(_):
            nonlocal call
            call += 1

            if call == 1:
                return string
            elif call == 2:
                return letter
            else:
                return ""

        return mock_input

    def test_input(self, mocker):
        """tests if input is invoked with the proper arguments"""

        mocker.patch("builtins.input")

        importlib.reload(
            importlib.import_module(name="input_replace", package="files"),
        )

        expected_outputs = (
            "文字列入力: ",
            "記号入力: ",
        )

        input.assert_has_calls(
            [mocker.call(expected_output) for expected_output in expected_outputs]
        )

    @pytest.mark.parametrize(
        "string, letter, result",
        [
            (
                "more python programming please",
                "§",
                "§ore python progra§§ing please",
            ),
            (
                "so many countries, so many customs",
                " ",
                " o many countrie ,  o many cu tom ",
            ),
        ],
    )
    def test_print(self, string, letter, result, mocker):
        """tests if print is invoked with the proper arguments"""

        mocker.patch(
            "builtins.input",
            self._mock_input_factory(
                string=string,
                letter=letter,
            ),
        )
        mocker.patch("builtins.print")

        importlib.reload(
            importlib.import_module(name="input_replace", package="files"),
        )

        expected_outputs = (
            "結果:",
            result,
        )

        print.assert_called_once_with(*expected_outputs)
