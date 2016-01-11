#!/bin/env python3

import sys
import time

from pytity.manager import Manager

import pigule.constants as constants
import pigule.archetypes as archetypes
from pigule.components import Clonable
from pigule.processors import Attack, MoodSwings, Reproduction, Time, Weather


if __name__ == '__main__':
    manager = Manager()

    attack = Attack(frequence=4, max_to_kill=2)
    attack.register_to(manager)
    MoodSwings().register_to(manager)
    Reproduction().register_to(manager)
    Time().register_to(manager)
    Weather(constants.WEATHER_SUNNY, 10).register_to(manager)

    master_cell = archetypes.create_master_cell(manager)
    clonable = master_cell.get_component(Clonable)

    is_running = True
    time_to_sleep = 1
    delta = 1
    while is_running:
        number_of_cells = len(list(manager.entities()))
        current_weather = '☀' if manager.environment['weather'] == constants.WEATHER_SUNNY else '☔'
        print('\rNumber of cells: {0:3d} (weather: {1})'.format(number_of_cells, current_weather), end='')
        sys.stdout.flush()

        try:
            time.sleep(time_to_sleep)
            manager.update(delta)
        except KeyboardInterrupt as e:
            is_running = False
            print('\nThis is the end...')

        if number_of_cells >= 25:
            attack.frequence = 2
        if number_of_cells <= 5 and attack.frequence == 2:
            clonable.fertility += 1
        if number_of_cells >= 60:
            attack.max_to_kill = 11

        if number_of_cells <= 0:
            is_running = False
            print('\nLooser...')
