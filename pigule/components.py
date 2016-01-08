from pytity.component import Component


class Clonable(Component):
    """Define if an entity can be cloned or not
    """
    def __init__(self):
        Component.__init__(self, True)
