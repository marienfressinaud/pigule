import sys
import time

from pytity.manager import Manager

import pigule.archetypes as archetypes
from pigule.processors import Reproduction


if __name__ == '__main__':
    manager = Manager()
    archetypes.create_master_cell(manager)

    Reproduction().register_to(manager)

    is_running = True
    delta = 1
    while is_running:
        try:
            number_of_cells = len(list(manager.entities()))
            print('\rNumber of cells: {}'.format(number_of_cells), end='')
            sys.stdout.flush()

            time.sleep(delta)
            manager.update(delta)
        except KeyboardInterrupt as e:
            is_running = False
            print('\nThis is the end...')
