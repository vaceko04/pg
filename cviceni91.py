def prevod_c_na_f(stupne):
    f = (stupne * 9/5) + 32
    return f


def test_prevodd_c_na_f():
    assert prevod_c_na_f(0) == 32
    assert prevod_c_na_f(100) == 212

if __name__ == "__main__":
    test_prevodd_c_na_f()