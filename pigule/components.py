from pytity.component import Component


class Age(Component):
    """Define the age of a cell
    """
    def __init__(self):
        Component.__init__(self, 0)

    def inc(self, value=1):
        self.value += value


class Clonable(Component):
    """Define if a cell can be cloned or not
    """
    def __init__(self):
        Component.__init__(self, True)


class Mortality(Component):
    """Define when a cell should die
    """
    def __init__(self, at):
        Component.__init__(self, at)
        self.die_at = at
