def test_say_hello(mocker):
    from fix_function_definition import say_hello

    expected_output = "Hello Alex!"

    assert say_hello("Alex") == expected_output
