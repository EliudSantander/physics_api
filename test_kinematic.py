import pytest
from kinematic import KinematicsEngine, PhysicsResultDTO

def test_mru_consistency():
    engine = KinematicsEngine()
    distance = engine.mru(v=10, t=5)
    assert distance == 50

def test_vertical_launch_peak():
    """
    Test a launch where v0=9.81 and g=9.81. 
    It should take 1s to reach the peak and 1s to return (2s total).
    """
    engine = KinematicsEngine()
    # Testing from h=0
    res = engine.get_vertical_data(v0=9.81, h=0, g=9.81)
    
    assert res.total_time == pytest.approx(2.0)
    assert res.max_height == pytest.approx(4.905)
    assert res.final_velocity_y == pytest.approx(9.81)
    assert res.initial_velocity_y == pytest.approx(9.81)

def test_parabolic_45_degrees():
    """
    At 45 degrees, initial vx and vy must be equal.
    """
    engine = KinematicsEngine()
    v0 = 100
    res = engine.get_parabolic_data(v0=v0, angulo_grados=45, h=0, g=9.81)
    
    # Using math: 100 * cos(45) should equal 100 * sin(45)
    assert res.velocity_x == pytest.approx(res.initial_velocity_y)
    # Range should be positive
    assert res.distance_x > 0