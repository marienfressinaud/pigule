from pigule.components import Clonable


def create_master_cell(manager):
    """Create a master cell

    A master cell can be cloned to give birth to "normal" cells.

    """
    cell = manager.create_entity()
    cell.add_component(Clonable(True))

    return cell
