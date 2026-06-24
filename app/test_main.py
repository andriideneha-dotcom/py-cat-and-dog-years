import app.main as main


def test_get_human_age_zero() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_get_human_age_first_year() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_get_human_age_second_year() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_get_human_age_third_year() -> None:
    assert main.get_human_age(15, 15) == [0, 0]
