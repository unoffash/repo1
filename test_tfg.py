import pytest
from example import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

if __name__ == "__main__":
    pytest.main()
