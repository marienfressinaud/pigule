import pytest

from pytity.manager import Manager

import pigule.constants as constants
import pigule.archetypes as archetypes


@pytest.fixture
def manager():
    return default_manager()


@pytest.fixture
def manager_with_master_cell():
    manager = default_manager()
    archetypes.create_master_cell(manager)
    return manager


def default_manager():
    manager = Manager()
    manager.environment['weather'] = constants.WEATHER_SUNNY
    return manager
