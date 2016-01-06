from pytity.manager import Manager

import pigule.archetypes as archetypes
from pigule.components import Clonable
from pigule.processors import Reproduction


def test_reproduction():
    manager = Manager()
    archetypes.create_master_cell(manager)

    assert len(list(manager.entities())) == 1

    Reproduction().register_to(manager)
    manager.update(1)

    assert len(list(manager.entities())) == 2


def test_reproduction_does_not_create_master_cell():
    manager = Manager()
    archetypes.create_master_cell(manager)

    Reproduction().register_to(manager)
    manager.update(1)

    assert len(list(manager.entities_by_type(Clonable))) == 1
