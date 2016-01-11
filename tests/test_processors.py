import pigule.constants as constants
from pigule.components import Age, Clonable, Mood, Mortality
from pigule.processors import MoodSwings, Reproduction, Time, Weather


def test_mood_swings(manager):
    cell = manager.create_entity()
    mood = Mood(manager.environment['weather'])
    cell.add_component(mood)
    MoodSwings().register_to(manager)

    assert mood.value == constants.MOOD_HAPPY

    manager.environment['weather'] = constants.WEATHER_RAINY
    manager.update(1)

    assert mood.value == constants.MOOD_SAD


def test_reproduction(manager_with_master_cell):
    Reproduction().register_to(manager_with_master_cell)
    manager_with_master_cell.update(1)

    assert len(list(manager_with_master_cell.entities())) == 2
    assert len(list(manager_with_master_cell.entities_by_type(Clonable))) == 1


def test_reproduction_impacted_by_mood_swings(manager_with_master_cell):
    MoodSwings().register_to(manager_with_master_cell)
    Reproduction().register_to(manager_with_master_cell)
    manager_with_master_cell.environment['weather'] = constants.WEATHER_RAINY
    expected_number_cloned = int(4 * constants.MOOD_IMPACT[constants.MOOD_SAD])

    manager_with_master_cell.update(4)

    assert len(list(manager_with_master_cell.entities())) == 1 + expected_number_cloned


def test_time(manager):
    cell = manager.create_entity()
    age = Age()
    cell.add_component(age)
    Time().register_to(manager)

    manager.update(10)

    assert age.value == 10


def test_time_kills_cells(manager):
    cell = manager.create_entity()
    cell.add_component(Age())
    cell.add_component(Mortality(10))
    Time().register_to(manager)

    manager.update(10)

    assert len(list(manager.entities())) == 0


def test_weather(manager):
    weather = Weather(constants.WEATHER_SUNNY, 10)
    weather.register_to(manager)

    assert weather.current_weather == constants.WEATHER_SUNNY
    manager.update(10)
    assert weather.current_weather == constants.WEATHER_RAINY
    manager.update(10)
    assert weather.current_weather == constants.WEATHER_SUNNY


def test_weather_does_not_update_if_cycle_is_incomplete(manager):
    weather = Weather(constants.WEATHER_SUNNY, 10)
    weather.register_to(manager)

    manager.update(5)
    assert weather.current_weather == constants.WEATHER_SUNNY
    manager.update(5)
    assert weather.current_weather == constants.WEATHER_RAINY
    manager.update(5)
    assert weather.current_weather == constants.WEATHER_RAINY


def test_weather_is_aware_of_long_delta_gap(manager):
    weather = Weather(constants.WEATHER_SUNNY, 10)
    weather.register_to(manager)

    manager.update(20)
    assert weather.current_weather == constants.WEATHER_SUNNY


def test_weather_maintains_manager_environment_up_to_date(manager):
    weather = Weather(constants.WEATHER_RAINY, 10)
    weather.register_to(manager)

    assert manager.environment['weather'] == constants.WEATHER_RAINY
    manager.update(10)
    assert manager.environment['weather'] == constants.WEATHER_SUNNY
