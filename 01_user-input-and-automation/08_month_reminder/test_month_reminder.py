import importlib
import subprocess

import pytest


class TestMonthReminder:
    @pytest.mark.parametrize(
        "number, month",
        [
            ("1", "January"),
            ("2", "February"),
            ("3", "March"),
            ("4", "April"),
            ("5", "May"),
            ("6", "June"),
            ("7", "July"),
            ("8", "August"),
            ("9", "September"),
            ("10", "October"),
            ("11", "November"),
            ("12", "December"),
        ],
    )
    def test_print(self, number, month, capfd):
        completed_process = subprocess.run(
            ["python", "month_reminder.py"],
            input=number,
            text=True,
        )
        captured = capfd.readouterr()

        assert completed_process.returncode == 0
        assert captured.out.strip() == month
        assert captured.err.strip() == ""

    @pytest.mark.parametrize(
        "number, month",
        [
            ("-1", "Error"),
            ("0", "Error"),
            ("13", "Error"),
        ],
    )
    def test_error(self, number, month, capfd):
        completed_process = subprocess.run(
            ["python", "month_reminder.py"],
            input=number,
            text=True,
        )
        captured = capfd.readouterr()

        assert completed_process.returncode == 0
        assert captured.out.strip() == month
        assert captured.err.strip() == ""
