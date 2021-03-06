#!/bin/env python3

import time

import daemonize

from pytity.manager import Manager

import pigule.constants as constants
from pigule.processors import Attack, MoodSwings, Reproduction, Time, Weather

import pigule.api.handler as api_handler


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

        self.api_server_thread = api_handler.setup(self.manager)

    def run(self):
        self.api_server_thread.start()

        while self.is_running:
            time.sleep(Game.TIME_TO_SLEEP)
            self.manager.update(Game.DELTA)

        self.api_server_thread.stop()

    def stop(self):
        self.is_running = False


if __name__ == '__main__':
    daemon_game = daemonize.daemonize(Game)
    daemon_game.execute()
