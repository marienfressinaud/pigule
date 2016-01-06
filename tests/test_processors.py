from pigule.components import Clonable
from pigule.processors import Reproduction


def test_reproduction(manager_with_master_cell):
    Reproduction().register_to(manager_with_master_cell)
    manager_with_master_cell.update(1)

    assert len(list(manager_with_master_cell.entities())) == 2
    assert len(list(manager_with_master_cell.entities_by_type(Clonable))) == 1
