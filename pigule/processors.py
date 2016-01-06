from pytity.processor import Processor

import pigule.archetypes as archetypes
from pigule.components import Clonable


class Reproduction(Processor):
    def update(self, delta):
        clonable_entities = list(self.manager.entities_by_type(Clonable))
        archetypes.create_cells(self.manager, len(clonable_entities))
