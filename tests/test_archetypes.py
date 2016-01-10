import pigule.archetypes as archetypes
from pigule.components import Age, Clonable, Mortality


def test_create_master_cell(manager):
    master_cell = archetypes.create_master_cell(manager)

    assert master_cell.get_component(Clonable) is not None
    assert master_cell.get_component(Age) is not None
    assert master_cell.get_component(Mortality) is None


def test_create_cells(manager):
    archetypes.create_cells(manager, 2)

    assert len(list(manager.entities())) == 2
    assert len(list(manager.entities_by_type(Clonable))) == 0
    assert len(list(manager.entities_by_type(Age))) == 2
    assert len(list(manager.entities_by_type(Mortality))) == 2
