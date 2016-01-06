from pytity.manager import Manager

import pigule.archetypes as archetypes
from pigule.components import Clonable


def test_create_master_cell():
    manager = Manager()

    master_cell = archetypes.create_master_cell(manager)

    assert master_cell.get_component(Clonable) is not None
