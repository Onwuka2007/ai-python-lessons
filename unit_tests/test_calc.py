from learn_lists.learn import calc_square
import pytest

def test_positive():
    assert calc_square(2) == 4
    assert calc_square(3) == 9
    
def test_negative():
    assert calc_square(-2) == 4
    assert calc_square(-3) == 9
    
def test_zero():
    assert calc_square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        assert calc_square('')
                    
# @pytest.mark.parametrize("input_val, expected", [
#     (2, 4),
#     (3, 9),
#     (-2, 4),
#     (0, 0)
# ])
# def test_calc_square(input_val, expected):
#     assert calc_square(input_val) == expected