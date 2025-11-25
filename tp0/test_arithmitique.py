import tp0.arithmetique as arithmetique
import pytest

def test_dlldk():
    assert arithmetique.valabs(5)==5
    assert arithmetique.valabs(-5)==5
    assert arithmetique.valabs(-22)==22


@pytest.mark.parametrize("arg,expected", [(-3, True), (3, True), (5, True), (10, False),(-10, False)])
def test_uneven(arg, expected):
    assert arithmetique.isuneven(arg) == expected

@pytest.fixture
def num() -> int:
    return 21 * 2

@pytest.mark.parametrize('k', list(range(9)))
def test_mk(num, k):
    assert arithmetique.prodmod(num * k, 5, num) == 0

@pytest.mark.parametrize('mul42', [i*42 for i in range(1,9)])
@pytest.mark.parametrize('div42', [1,2,3,6,7,21,42])
def test_div(mul42, div42):
    assert arithmetique.divis(mul42, div42)

def test_error():
    with pytest.raises(ZeroDivisionError):
        arithmetique.prodmod(3, 5, 0)