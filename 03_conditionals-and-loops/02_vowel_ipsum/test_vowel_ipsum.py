import importlib


def test_vowel_ipsum(mocker):
    mocker.patch("builtins.print")
    importlib.import_module(name="vowel_ipsum", package="files")

    expected_output = 165
    print.assert_called_once_with(expected_output)
