from pytity.processor import EntityProcessor, Processor

import pigule.archetypes as archetypes
from pigule.components import Age, Clonable, Mortality


class Reproduction(Processor):
    """Manage reproduction of clonable cells
    """
    def update(self, delta):
        clonable_cells = list(self.manager.entities_by_type(Clonable))
        archetypes.create_cells(self.manager, len(clonable_cells))


class Time(EntityProcessor):
    """Manage time-based operations such as cell age or mortality
    """
    def __init__(self):
        EntityProcessor.__init__(self)
        self.needed = [Age]

    def update_entity(self, delta, cell):
        age = cell.get_component(Age)
        age.inc(delta)

        mortality = cell.get_component(Mortality)
        if mortality is not None and age.value >= mortality.die_at:
            self.manager.kill_entity(cell)


class Weather(Processor):
    """Manage weather of the game
    """
    SUNNY = 'sunny'
    RAINY = 'rainy'

    def __init__(self, initial_weather, cycle_frequence):
        Processor.__init__(self)
        self.current_weather = initial_weather
        self.cycle_frequence = cycle_frequence
        self.current_cycle = 0

    def update(self, delta):
        delta_from_last_update = self.current_cycle + delta
        switch_number = delta_from_last_update // self.cycle_frequence

        if switch_number % 2 == 1:
            self.current_weather = self.switch(self.current_weather)

        self.current_cycle = delta_from_last_update % self.cycle_frequence

    def switch(self, weather):
        return self.RAINY if weather == self.SUNNY else self.SUNNY
