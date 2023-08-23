import importlib


def test_inspiring_quotes(mocker):
    mocker.patch("builtins.print")

    importlib.import_module(name="inspiring_quotes", package="files")

    expected_outputs = [
        '"I do not fear computers.I fear lack of them." - Asimov, Isaac',
        '"A computer once beat me at chess, but it was no match for me at kick boxing." - Philips, Emo',
        '"Computer Science is no more about computers than astronomy is about telescopes." - Dijkstra, Edsger',
        '"The computer was born to solve problems that did not exist before." - Gates, Bill',
        '"Software is like entropy:It is difficult to grasp, weighs nothing, and obeys the Second Law of Thermodynamics; i.e., it always increases." - Augustine, Norman',
        '"Software is a gas; it expands to fill its container." - Myhrvold, Nathan',
        '"Standards are always out of date. That’s what makes them standards." - Bennett, Alan',
    ]

    print.assert_has_calls(
        [mocker.call(expected_output) for expected_output in expected_outputs]
    )
