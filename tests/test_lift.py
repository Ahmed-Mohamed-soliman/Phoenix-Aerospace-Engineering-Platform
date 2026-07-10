from src.physics.lift import calculate_lift


def test_calculate_lift():
    lift = calculate_lift(
        rho=1.225,
        velocity=70,
        wing_area=16,
        cl=0.5
    )

    expected = 24010.0

    assert abs(lift - expected) < 0.01
