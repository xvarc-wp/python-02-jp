import importlib

import pytest


class TestInvestments:
    @pytest.fixture
    def input_arguments(self):
        return [
            "Enter the investment amount (in USD): ",
            "Enter the interest rate (in percentage): ",
            "Enter the number of years to invest: ",
        ]

    @pytest.fixture
    def counter(self):
        called_times = -1

        def inner_counter():
            nonlocal called_times
            called_times += 1
            return called_times

        return inner_counter

    def test_input(self, mocker, input_arguments):
        mocker.patch("builtins.input")

        importlib.reload(
            importlib.import_module(
                name="investments",
                package="files",
            )
        )

        # assert_has_calls might fail if a learner directly converts data type of the return value of input function
        input.called_with(
            *[mocker.call(input_argument) for input_argument in input_arguments]
        )

    @pytest.mark.parametrize(
        "actual_inputs, expected_output",
        [
            (
                ["10000", "10", "10"],
                "Future value after 10 years: $25937.42",
            ),
            (
                ["2000", "5", "30"],
                "Future value after 30 years: $8643.88",
            ),
        ],
    )
    def test_print(
        self,
        mocker,
        counter,
        actual_inputs,
        expected_output,
    ):
        mocker.patch("builtins.input", lambda _: actual_inputs[counter()])
        mocker.patch("builtins.print")

        importlib.reload(
            importlib.import_module(
                name="investments",
                package="files",
            )
        )

        print.assert_called_once_with(expected_output)
