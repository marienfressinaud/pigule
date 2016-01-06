import pytest

from pytity.manager import Manager

import pigule.archetypes as archetypes


@pytest.fixture
def manager():
    return Manager()


@pytest.fixture
def manager_with_master_cell():
    manager = Manager()
    archetypes.create_master_cell(manager)
    return manager
