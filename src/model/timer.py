#!/usr/bin/env python3
import threading
import logging

from code.dust import Main

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)


class Repetition :
    def __init__(self):
        self.timer = None

    def start(self, f, delay=Main.DELAY):
        def fn():
            f()
            self.timer = threading.Timer(delay, fn)
            logger.info('start timer delay {}'.format(delay))
            self.timer.start()
        fn()

    def cancel(self):
        if self.timer:
            logger.info('cancel timer')
            self.timer.cancel()

