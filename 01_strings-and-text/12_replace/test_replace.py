expected = """10

_aggie and _illy and _olly and _ay
went down to the beach(to play one day)

and _aggie discovered a shell that sang
so sweetly she couldn't re_e_ber her troubles,and

_illy befriended a stranded star
whose rays five languid fingers were;

and _olly was chased by a horrible thing
which raced sideways while blowing bubbles:and

_ay ca_e ho_e with a s_ooth round stone
as s_all as a world and as large as alone.

For whatever we lose(like a you or a _e)
it's always ourselves we find in the sea"""


def test_replace():
    import replace

    assert replace.poem == expected
