#!/bin/env python3

import sys
import time

import daemonize

from pytity.manager import Manager

import pigule.constants as constants
import pigule.archetypes as archetypes
from pigule.components import Clonable
from pigule.processors import Attack, MoodSwings, Reproduction, Time, Weather


class Game:
    TIME_TO_SLEEP = 1
    DELTA = 1

    def __init__(self):
        self.is_running = True
        self.manager = Manager()

        self.attack = Attack(frequence=4, max_to_kill=2)
        self.attack.register_to(self.manager)
        MoodSwings().register_to(self.manager)
        Reproduction().register_to(self.manager)
        Time().register_to(self.manager)
        Weather(constants.WEATHER_SUNNY, 10).register_to(self.manager)

        self.master_cell = archetypes.create_master_cell(self.manager)
        self.clonable = self.master_cell.get_component(Clonable)

    def run(self):
        while self.is_running:
            time.sleep(Game.TIME_TO_SLEEP)
            self.manager.update(Game.DELTA)
            number_of_cells = len(list(self.manager.entities()))
            current_weather = '☀' if self.manager.environment['weather'] == constants.WEATHER_SUNNY else '☔'
            print('Number of cells: {0:3d} (weather: {1})'.format(number_of_cells, current_weather))
            sys.stdout.flush()

            number_of_cells = len(list(self.manager.entities()))
            if number_of_cells >= 25:
                self.attack.frequence = 2
            if number_of_cells <= 5 and self.attack.frequence == 2:
                self.clonable.fertility += 1
            if number_of_cells >= 60:
                self.attack.max_to_kill = 11

            if number_of_cells <= 0:
                self.stop()
                print('Looser...')

    def stop(self):
        self.is_running = False
        print('This is the end...')


if __name__ == '__main__':
    game = Game()
    daemon_game = daemonize.daemonize(game)
    daemon_game.execute()
