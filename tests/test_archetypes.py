import pigule.archetypes as archetypes
from pigule.components import Clonable


def test_create_master_cell(manager):
    master_cell = archetypes.create_master_cell(manager)

    assert master_cell.get_component(Clonable) is not None


def test_create_cells(manager):
    archetypes.create_cells(manager, 2)

    assert len(list(manager.entities())) == 2
    assert len(list(manager.entities_by_type(Clonable))) == 0
