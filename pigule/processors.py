from pytity.processor import EntityProcessor, Processor

import pigule.archetypes as archetypes
from pigule.components import Age, Clonable, Mortality


class Reproduction(Processor):
    """Manage reproduction of clonable cells
    """
    def update(self, delta):
        clonable_entities = list(self.manager.entities_by_type(Clonable))
        archetypes.create_cells(self.manager, len(clonable_entities))


class Time(EntityProcessor):
    """Manage time-based operations such as cell age or mortality
    """
    def __init__(self):
        EntityProcessor.__init__(self)
        self.needed = [Age]

    def update_entity(self, delta, entity):
        age = entity.get_component(Age)
        age.inc(delta)

        mortality = entity.get_component(Mortality)
        if mortality is not None and age.value >= mortality.die_at:
            self.manager.kill_entity(entity)
