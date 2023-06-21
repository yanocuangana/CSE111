from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest

def test_water_column_height():
    water = water_column_height(0, 0)
    assert water == approx(0)

    water = water_column_height(0, 10)
    assert water == approx(7.5)

    water = water_column_height(25, 0)
    assert water == approx(25)

    water = water_column_height(48.3, 12.8)
    assert water == approx(57.9)

def test_pressure_gain_from_water_height():
    
    p = pressure_gain_from_water_height(0)
    assert p == approx(0 , abs= 0.001)

    p = pressure_gain_from_water_height(30.2)
    assert p == approx(295.628 , abs= 0.001)

    p = pressure_gain_from_water_height(50)
    assert p == approx(489.450 , abs= 0.001)

def test_pressure_loss_from_pipe():

    p = pressure_loss_from_pipe(0.048692, 0,  0.018, 1.75)
    assert p == approx(0 , abs= 0.001)

    p = pressure_loss_from_pipe(0.048692, 200,  0, 1.75)
    assert p == approx(0 , abs= 0.001)

    p = pressure_loss_from_pipe(0.048692, 200,  0.018, 0)
    assert p == approx(0 , abs= 0.001)

    p = pressure_loss_from_pipe(0.048692, 200,  0.018, 1.75)
    assert p == approx(-113.008 , abs= 0.001)

    p = pressure_loss_from_pipe(0.048692, 200,  0.018, 1.65)
    assert p == approx(-100.462 , abs= 0.001)

    p = pressure_loss_from_pipe(0.28687, 1000,  0.013, 1.65)
    assert p == approx(-61.576 , abs= 0.001)

    p = pressure_loss_from_pipe(0.28687, 1800.75,  0.013, 1.65)
    assert p == approx(-110.884 , abs= 0.001)





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])