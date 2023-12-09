from repeat_string import repeat_string

def test_sum1():
    result = repeat_string("hello", 2, 3)
    assert result == "hellohello\nhellohello\nhellohello"