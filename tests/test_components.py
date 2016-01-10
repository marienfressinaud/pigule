from pigule.components import Clonable


def test_clonable_incubate():
    clonable = Clonable()

    number_to_clone = clonable.incubate(1)

    assert number_to_clone == 1


def test_clonable_incubate_depends_on_fertility():
    clonable = Clonable(fertility=0.5)

    assert clonable.incubate(1) == 0
    assert clonable.incubate(1) == 1


def test_clonable_incubate_depends_on_time():
    clonable = Clonable()

    assert clonable.incubate(1) == 1
    assert clonable.incubate(2) == 2
    assert clonable.incubate(42) == 42
