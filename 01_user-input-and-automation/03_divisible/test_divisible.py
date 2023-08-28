import subprocess
from pathlib import Path

import pytest


class TestDivisible:
    parent = Path(__file__).resolve().parent
    file_path = f"{parent}/divisible.py"

    @pytest.mark.parametrize(
        "number, expected_output",
        [
            ("0", "The number needs to be between 1 and 1,000,000,000."),
            ("1000000001", "The number needs to be between 1 and 1,000,000,000."),
        ],
    )
    def test_range(self, number, expected_output, capfd):
        completed_process = subprocess.run(
            ["python", self.file_path],
            input=number,
            text=True,
        )
        captured = capfd.readouterr()

        assert completed_process.returncode == 0
        assert captured.out.strip() == expected_output
        assert captured.err.strip() == ""

    @pytest.mark.parametrize(
        "number, expected_output",
        [
            ("3", "We can divide 3 by 3!"),
            ("999999999", "We can divide 999999999 by 3!"),
        ],
    )
    def test_divisible(self, number, expected_output, capfd):
        completed_process = subprocess.run(
            ["python", self.file_path],
            input=number,
            text=True,
        )
        captured = capfd.readouterr()

        assert completed_process.returncode == 0
        assert captured.out.strip() == expected_output
        assert captured.err.strip() == ""
        
    @pytest.mark.parametrize(
        "number, expected_output",
        [
            ("4", "We cannot divide 4 by 3..."),
            ("1000000000", "We cannot divide 1000000000 by 3..."),
        ],
    )
    def test_indivisible(self, number, expected_output, capfd):
        completed_process = subprocess.run(
            ["python", self.file_path],
            input=number,
            text=True,
        )
        captured = capfd.readouterr()

        assert completed_process.returncode == 0
        assert captured.out.strip() == expected_output
        assert captured.err.strip() == ""
        
