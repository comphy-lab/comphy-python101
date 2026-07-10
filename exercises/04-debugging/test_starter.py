from starter import steady_state_index


def test_false_two_point_plateau_is_rejected() -> None:
    values = [0.0, 1.0, 1.01, 2.0, 3.0, 4.0]
    assert steady_state_index(values, window=3) is None


def test_complete_plateau_is_found() -> None:
    values = [0.0, 1.0, 1.8, 2.0, 2.01, 1.99, 2.0]
    assert steady_state_index(values, window=4) == 6
