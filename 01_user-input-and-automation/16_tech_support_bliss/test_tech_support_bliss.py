import importlib


def test_support_bliss(mocker):
    import platform

    mocked_values = {
        "platform": "macOS-13.5",
        "python_compiler": "Clang 14.0.0",
        "python_version": "3.10.2",
        "system": "Darwin",
        "release": "22.6.0",
        "processor": "arm",
    }

    mocker.patch.multiple(
        "platform",
        **{key: lambda val=val: val for key, val in mocked_values.items()},
    )

    mocker.patch("builtins.print")
    importlib.import_module(name="tech_support_bliss", package="files")

    expected_outputs = [
        f"{'Platform:':>10} {mocked_values['platform']}",
        f"{'Compiler:':>10} {mocked_values['python_compiler']}",
        f"{'Python:':>10} {mocked_values['python_version']}",
        f"{'System:':>10} {mocked_values['system']}",
        f"{'Release:':>10} {mocked_values['release']}",
        f"{'System:':>10} {mocked_values['processor']}",
    ]
    print.assert_has_calls(
        [mocker.call(expected_output) for expected_output in expected_outputs]
    )
