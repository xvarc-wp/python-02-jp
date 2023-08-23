import importlib


class TestFormatme:
    def test_animal(self):
        """Test if a variable animal has the proper value"""
        import formatme

        assert formatme.animal == "cat"

    def test_print(self, mocker):
        """Test if print is called"""

        mocker.patch("builtins.print")
        importlib.reload(
            importlib.import_module(name="formatme", package="files"),
        )

        expected_output = "The cat (Felis catus) is a domestic species of small carnivorous mammal.It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family."

        print.assert_called_once_with(expected_output)
