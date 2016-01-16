#!/bin/env python3

import time

import daemonize

from pytity.manager import Manager

import pigule.constants as constants
import pigule.archetypes as archetypes
from pigule.processors import Attack, MoodSwings, Reproduction, Time, Weather


class Game:
    TIME_TO_SLEEP = 1
    DELTA = 1

    def __init__(self):
        self.is_running = True
        self.manager = Manager()

        Attack(frequence=4, max_to_kill=2).register_to(self.manager)
        MoodSwings().register_to(self.manager)
        Reproduction().register_to(self.manager)
        Time().register_to(self.manager)
        Weather(constants.WEATHER_SUNNY, 10).register_to(self.manager)

    def run(self):
        archetypes.create_master_cell(self.manager)

        while self.is_running:
            time.sleep(Game.TIME_TO_SLEEP)
            self.manager.update(Game.DELTA)

    def stop(self):
        self.is_running = False


if __name__ == '__main__':
    daemon_game = daemonize.daemonize(Game)
    daemon_game.execute()
