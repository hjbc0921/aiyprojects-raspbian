from dust.dust import (get_dust, get_dust_level)
import code.dust as dust_code


def check_words(t, words):
    return any(word in t for word in words)


def execute_dust(text, say, turn_on):
    state = None
    for code, state_words in dust_code.State.list.items():
        if check_words(text, state_words):
            state = code
            break

    dust_value = get_dust(state) if state else get_dust()
    level = get_dust_level(dust_value)

    say(dust_code.Level.list[level])
    turn_on(dust_code.Color.list[level])


def stop_dust(say, turn_off):
    say()
    turn_off()


def dust(text, say, turn_on, turn_off):
    if '켜' in text:
        execute_dust(text, say, turn_on)
    elif '꺼' in text:
        stop_dust(say, turn_off)
    else:
        execute_dust(text, say, turn_on)
