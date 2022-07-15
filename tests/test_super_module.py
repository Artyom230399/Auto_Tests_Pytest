import pytest

from app.super_module import super_sum


#   cond - входные данные.  exp - ожидаемый результат
@pytest.mark.parametrize("cond, exp", [
    ((1, 2), 3),
    ((-1, 2), 1),
    ((0, -1), -1),
    ((2, 0), 2)
])
def test_poositive1(cond, exp):
    assert super_sum(cond[0], cond[1]) == exp  # [assert super_sum(*cond) == exp] * - распаковка


'''
def test_poositive2():
    assert super_sum(-1, 2) == 1


def test_poositive3():
    assert super_sum(0, -1) == -1


def test_poositive4():
    assert super_sum(2, 0) == 2
'''
