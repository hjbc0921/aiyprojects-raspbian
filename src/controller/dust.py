#!/usr/bin/env python3
from model.dust import (get_dust, get_dust_level)
from model.timer import Repetition
import code.dust as dust_code


def check_words(t, words):
    return any(word in t for word in words)


timer = Repetition()


def on_dust(text, say, turn_on):
    state = None
    for code, state_words in dust_code.State.list.items():
        if check_words(text, state_words):
            state = code
            break

    def on():
        dust_value = get_dust(state) if state else get_dust()
        level = get_dust_level(dust_value)

        say(dust_code.Level.list[level])
        turn_on(dust_code.Color.list[level])

    timer.cancel()
    timer.start(on)


def off_dust(say, turn_off):
    say(dust_code.Main.TURN_OFF)
    turn_off()
    timer.cancel()


def dust(text, say, turn_on, turn_off):
    if check_words(text, dust_code.Main.ON):
        on_dust(text, say, turn_on)
    elif check_words(text, dust_code.Main.OFF):
        off_dust(say, turn_off)
    else:
        on_dust(text, say, turn_on)


if __name__ == '__main__':
    while True:
        dust(input('You say:'),
             lambda x: print('SAY: {}'.format(x)),
             lambda x: print('ON: {}'.format(x)),
             lambda: print('OFF'))
