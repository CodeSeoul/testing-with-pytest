import pytest

from src.maths.pythagoras import pythagoras_calculate_hypotenuse


def test_pythagoras_slow_manual_boring():
    # set up and run code
    result = pythagoras_calculate_hypotenuse(a=3, b=4)

    # verify
    assert result == 5


def test_pythagoras_with_for_loop():
    # set up
    test_cases = [
        (3, 4, 5),
        (5, 12, 13),
        (7, 24, 25),
        (8, 15, 17),
        (9, 40, 41),
        (11, 60, 61),
        (12, 35, 37),
        (13, 84, 85),
        (16, 63, 65),
        (20, 21, 29),
        (28, 45, 53),
        (33, 56, 65),
        (36, 77, 85),
        (39, 80, 89),
        (48, 55, 73),
        (65, 72, 97),
    ]
    for side1, side2, hypotenuse in test_cases:
        # run code
        result = pythagoras_calculate_hypotenuse(a=side1, b=side2)

        # verify
        assert result == hypotenuse


@pytest.mark.parametrize(
    "side1, side2, hypotenuse",
    [
        (3, 4, 5),
        (5, 12, 13),
        (7, 24, 25),
        (8, 15, 17),
        (9, 40, 41),
        (11, 60, 61),
        (12, 35, 37),
        (13, 84, 85),
        (16, 63, 65),
        (20, 21, 29),
        (28, 45, 53),
        (33, 56, 65),
        (36, 77, 85),
        (39, 80, 89),
        (48, 55, 73),
        (65, 72, 97),
    ],
)  # set up
def test_pythagoras_cooler_and_faster_with_parameterize(
    side1: int,
    side2: int,
    hypotenuse: int,
):
    # run code
    result = pythagoras_calculate_hypotenuse(a=side1, b=side2)

    # verify
    assert result == hypotenuse
