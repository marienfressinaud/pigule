from pytity.component import Component

import pigule.constants as constants


class Age(Component):
    """Define the age of a cell
    """
    def __init__(self):
        Component.__init__(self, 0)

    def inc(self, value=1):
        self.value += value


class Clonable(Component):
    """Define fertility of a cell and frequency of its "clonability"
    """
    def __init__(self, fertility=1):
        Component.__init__(self, fertility)
        self.fertility = fertility
        self.time_of_incubation = 0

    def incubate(self, time):
        self.time_of_incubation += self.fertility * time
        number_to_clone = int(self.time_of_incubation)
        self.time_of_incubation %= 1

        return number_to_clone


class Mood(Component):
    """Define the mood of a cell
    """
    def __init__(self, weather):
        Component.__init__(self, None)
        self.weather_changing(weather)

    def weather_changing(self, weather):
        self.value = constants.MOOD_HAPPY if weather == constants.WEATHER_SUNNY else constants.MOOD_SAD


class Mortality(Component):
    """Define when a cell should die
    """
    def __init__(self, at):
        Component.__init__(self, at)
        self.die_at = at
