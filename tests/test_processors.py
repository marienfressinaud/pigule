import pigule.constants as constants
from pigule.components import Age, Clonable, Mortality
from pigule.processors import Reproduction, Time, Weather


def test_reproduction(manager_with_master_cell):
    Reproduction().register_to(manager_with_master_cell)
    manager_with_master_cell.update(1)

    assert len(list(manager_with_master_cell.entities())) == 2
    assert len(list(manager_with_master_cell.entities_by_type(Clonable))) == 1


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
