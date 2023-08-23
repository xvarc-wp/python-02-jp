import importlib


def test_long_words(mocker):
    mocker.patch("builtins.print")

    importlib.import_module(
        name="long_words",
        package="files",
    )

    expected_outputs = [
        "counterdemonstrations",
        "hyperaggressivenesses",
        "microminiaturizations",
    ]

    print.assert_has_calls(
        [mocker.call(expected_output) for expected_output in expected_outputs],
    )
