import app.main as main


def test_get_human_age_zero() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_first_threshold() -> None:
    # менше 15 років → 0 людських років
    assert main.get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_year() -> None:
    # рівно 15 → 1 рік
    assert main.get_human_age(15, 15) == [1, 1]


def test_get_human_age_between_first_and_second() -> None:
    # 16–23 → все ще 1 рік
    assert main.get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_year_boundary() -> None:
    # 24 → 2 роки
    assert main.get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_different_growth_rules() -> None:
    # важливий тест: різні формули (4 vs 5)
    assert main.get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_values() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_cat_and_dog_different_inputs() -> None:
    # ще один важливий тест на асиметрію
    assert main.get_human_age(28, 32) == [3, 3]
