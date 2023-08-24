import importlib


class TestFlintScopes:
    def test_shout(self):
        from flintscopes import shout

        name = "Joh"
        expected_output = "JOH"

        assert shout(name) == expected_output

    def test_print(self, mocker):
        mocker.patch("builtins.print")

        expected_output = "WILMA"

        importlib.reload(
            importlib.import_module(
                name="flintscopes",
                package="files",
            ),
        )

        print.assert_called_once_with(expected_output)
