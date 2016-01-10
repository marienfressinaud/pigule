import pigule.constants as constants
from pigule.components import Clonable, Mood


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


def test_mood():
    assert Mood(constants.WEATHER_SUNNY).value == constants.MOOD_HAPPY
    assert Mood(constants.WEATHER_RAINY).value == constants.MOOD_SAD


def test_mood_weather_changing():
    mood = Mood(constants.WEATHER_SUNNY)
    mood.weather_changing(constants.WEATHER_RAINY)

    assert mood.value == constants.MOOD_SAD
