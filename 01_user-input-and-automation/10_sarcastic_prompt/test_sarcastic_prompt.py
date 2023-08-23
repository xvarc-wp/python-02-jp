import importlib
import subprocess

import pytest


class TestSarcasticPrompt:
    @pytest.mark.parametrize(
        "input_text, output_text",
        [
            ("Hello world!", "hElLo wOrLd!"),
            ("AAAAAAAAAA", "aAaAaAaAaA"),
            ("aaaaaaaaaa", "aAaAaAaAaA"),
            ("1234567890", "1234567890"),
        ],
    )
    def test_print(self, input_text, output_text, capfd):
        completed_process = subprocess.run(
            ["python", "sarcastic_prompt.py"],
            input=input_text,
            text=True,
        )
        captured = capfd.readouterr()

        assert completed_process.returncode == 0
        assert captured.out.strip() == output_text
        assert captured.err.strip() == ""
