import subprocess
from pathlib import Path

import pytest


class TestSarcasticPrompt:
    parent = Path(__file__).resolve().parent
    file_path = f"{parent}/sarcastic_prompt.py"

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
            ["python", self.file_path],
            input=input_text,
            text=True,
        )
        captured = capfd.readouterr()

        assert completed_process.returncode == 0
        assert captured.out.strip() == output_text
        assert captured.err.strip() == ""
