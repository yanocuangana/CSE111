from water_flow import water_column_height
from pytest import approx
import pytest

def test_water_column_height():
    height = water_column_height(0, 0)
    assert height == approx(0)

pytest.main(["-v", "--tb=line", "-rN", __file__])