import importlib


def test_office_supplies(mocker):
    mocker.patch("builtins.print")

    importlib.import_module(name="office_supplies", package="files")

    expected_outputs = [
        "Scott, Michael           world's best boss mug",
        "Schrute, Dwight          pepper spray",
        "Halpert, Jim             phone",
        "Beesly, Pam              post-its",
        "Howard, Ryan             business cards",
        "Hudson, Stanley          crossword-puzzle",
        "Malone, Kevin            m&ms",
        "Palmer, Meredith         flask",
        "Martin, Angela           cat food",
        "Martinez, Oscar          calculator",
        "Lapin, Phyllis           cut flowers",
        "Kapoor, Kelly            People magazine",
        "Flenderson, Toby         files",
        "Bratton, Creed           mung beans",
        "Philbin, Darryl          forklift",
    ]

    print.assert_has_calls(
        [mocker.call(expected_output) for expected_output in expected_outputs]
    )
