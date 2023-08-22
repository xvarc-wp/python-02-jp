import importlib


class NoErrorFound(Exception):
    pass


class InvalidError(Exception):
    pass


def test_new_friends_2(mocker):
    mocker.patch("builtins.print")
    try:
        importlib.import_module(name="new_friends_2", package="files")
    except TypeError:
        assert True
        return
    except Exception as e:
        raise InvalidError("The unexpected error is thrown: ", e)
    raise NoErrorFound("An error is not thrown!")
