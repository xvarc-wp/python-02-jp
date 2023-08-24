import importlib


def test_mind_the_order(mocker):
    mocker.patch("builtins.print")

    expected_outputs = [
        "For your own safety, please follow the instructions carefully:",
        "1. Take your parachute.",
        "2. JUMP!",
    ]

    importlib.import_module(
        name="mind_the_order",
        package="files",
    )

    print.assert_has_calls(
        [mocker.call(expected_output) for expected_output in expected_outputs]
    )
