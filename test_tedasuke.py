from tedasuke import tedasuke


def test_tedasuke():
    t = tedasuke("str ing", True)
    want = ["str", "ing"]
    result = t.split()
    assert want == result

    t = tedasuke("str ing", False)
    want = None
    result = t.split()
    assert want == result
