import subprocess

import pytest


@pytest.mark.parametrize(
    "text, expected_output",
    [
        (
            "He dropped the ball. While most people would think that this was a metaphor of some type, in Joe's case it was absolutely literal. He had hopes of reaching the Major League and that dream was now it great jeopardy. All because he had dropped the ball.",
            "the",
        ),
        (
            "'Can I get you anything else?' David asked. It was a question he asked a hundred times a day and he always received the same answer. It had become such an ingrained part of his daily routine that he had to step back and actively think when he heard the little girl's reply. Nobody had before answered the question the way that she did, and David didn't know how he should respond.",
            "he",
        ),
    ],
)
def test_split_and_pick(text, expected_output, capfd):
    completed_process = subprocess.run(
        ["python", "split_and_pick.py"],
        input=text,
        text=True,
    )
    captured = capfd.readouterr()

    assert completed_process.returncode == 0
    assert captured.out.strip() == expected_output
    assert captured.err.strip() == ""
