def test_flatten(mocker):
    import flatten

    expected_outputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert len(flatten.flattened_list) == len(expected_outputs)
    for i, expected_output in enumerate(expected_outputs):
        assert flatten.flattened_list[i] == expected_output
