def test_shorthands():
    """test if shorthands is 2

    This test does not guarantee that a learner uses shorthand assignment.
    """
    import shorthands

    assert shorthands.shorthands == 2
