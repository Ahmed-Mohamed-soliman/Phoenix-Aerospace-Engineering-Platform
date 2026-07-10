from src.physics.drag import calculate_drag


def test_calculate_drag():
    drag = calculate_drag(
        rho=1.225,
        velocity=70,
        wing_area=16,
        cd=0.03
    )

    expected = 1440.6

    assert abs(drag - expected) < 0.01
