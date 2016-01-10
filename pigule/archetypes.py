from pigule.components import Age, Clonable, Mortality


def create_master_cell(manager):
    """Create a master cell

    A master cell can be cloned to give birth to "normal" cells.

    """
    cell = manager.create_entity()
    cell.add_component(Age())
    cell.add_component(Clonable())

    return cell


def create_cells(manager, number_of_cells):
    """Create a list of basic cells
    """

    for i in range(number_of_cells):
        cell = manager.create_entity()
        cell.add_component(Age())
        # FIXME: define a constant for Mortality
        cell.add_component(Mortality(42))
