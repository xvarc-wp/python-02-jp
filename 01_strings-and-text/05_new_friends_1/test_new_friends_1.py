import importlib


class NoErrorFound(Exception):
    pass


class InvalidError(Exception):
    pass


def test_new_friends_1(mocker):
    mocker.patch("builtins.print")
    try:
        importlib.import_module(name="new_friends_1", package="files")
    except SyntaxError:
        assert True
        return
    except Exception as e:
        raise InvalidError("The unexpected error is thrown: ", e)
    raise NoErrorFound("An error is not thrown!")
