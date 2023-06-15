# Needed to resolve path issue to calculator module
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from calculator import add, div, mul, sub


def test_add():
    assert add(1, 1) == 2


def test_sub():
    assert sub(1, 1) == 0


def test_mul():
    assert mul(1, 1) == 1


def test_div():
    assert div(2, 1) == 2
