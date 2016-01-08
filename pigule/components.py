from pytity.component import Component


class Age(Component):
    """Define the age of an entity
    """
    def __init__(self):
        Component.__init__(self, 0)

    def inc(self, value=1):
        self.value += value


class Clonable(Component):
    """Define if an entity can be cloned or not
    """
    def __init__(self):
        Component.__init__(self, True)
