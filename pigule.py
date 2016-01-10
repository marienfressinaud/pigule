import sys
import time

from pytity.manager import Manager

import pigule.constants as constants
import pigule.archetypes as archetypes
from pigule.processors import Reproduction, Time, Weather


if __name__ == '__main__':
    manager = Manager()

    Reproduction().register_to(manager)
    Time().register_to(manager)
    weather = Weather(constants.WEATHER_SUNNY, 10)
    weather.register_to(manager)

    archetypes.create_master_cell(manager)

    is_running = True
    delta = 1
    while is_running:
        try:
            number_of_cells = len(list(manager.entities()))
            current_weather = '☀' if weather.current_weather == constants.WEATHER_SUNNY else '☔'
            print('\rNumber of cells: {0} (weather: {1})'.format(number_of_cells, current_weather), end='')
            sys.stdout.flush()

            time.sleep(delta)
            manager.update(delta)
        except KeyboardInterrupt as e:
            is_running = False
            print('\nThis is the end...')
