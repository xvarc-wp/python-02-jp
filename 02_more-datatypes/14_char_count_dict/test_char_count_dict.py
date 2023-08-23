import importlib

import pytest


@pytest.mark.parametrize(
    "text, expected_output",
    [
        (
            "hello",
            {"h": 1, "e": 1, "l": 2, "o": 1},
        ),
        (
            "supercalifragilisticexpialidocious",
            {
                "s": 3,
                "u": 2,
                "p": 2,
                "e": 2,
                "r": 2,
                "c": 3,
                "a": 3,
                "l": 3,
                "i": 7,
                "f": 1,
                "g": 1,
                "t": 1,
                "x": 1,
                "d": 1,
                "o": 2,
            },
        ),
    ],
)
def test_char_count_dict(mocker, text, expected_output):
    mocker.patch("builtins.input", lambda: text)
    import char_count_dict

    reloaded_module = importlib.reload(char_count_dict)

    assert reloaded_module.result == expected_output
