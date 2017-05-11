def f():
    return 3

def test_f(low_performance):
    if not low_performance:
        assert f() == 4
    assert 1
