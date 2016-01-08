from pigule.components import Age, Clonable
from pigule.processors import Reproduction, Time


def test_reproduction(manager_with_master_cell):
    Reproduction().register_to(manager_with_master_cell)
    manager_with_master_cell.update(1)

    assert len(list(manager_with_master_cell.entities())) == 2
    assert len(list(manager_with_master_cell.entities_by_type(Clonable))) == 1


def test_time(manager):
    entity = manager.create_entity()
    age = Age()
    entity.add_component(age)
    Time().register_to(manager)

    manager.update(10)

    assert age.value == 10
