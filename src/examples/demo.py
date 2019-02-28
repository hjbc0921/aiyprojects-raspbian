#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
import argparse
import locale
import logging

from controller.game import (updown, deohagi, gugudan)
# from controller.music import play_music
from controller.dust import dust

import code.game as game_code
import code.dust as dust_code


def play_music(num):
    print('>>>>>> {}번 노래 재생 중~~'.format(num))


def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('turn on the light',
                'turn off the light',
                'blink the light',
                'goodbye')
    return None


def locale_language():
    language, _ = locale.getdefaultlocale()
    return language


def say(text):
    print('>>>>>> {}'.format(text))


def recognize():
    text = input('<<<<<< ')
    return text.lower()


def main():
    logging.basicConfig(level=logging.DEBUG)

    def check_word(t, words):
        return any(word in t for word in words)

    def hear():
        return recognize()

    def success():
        print('****** 초록불 깜빡깜빡 ******')

    def fail():
        print('****** 빨간불 깜빡깜빡 ******')

    while True:
        text = hear()
        logging.info('You said: "%s"' % text)

        if game_code.Main.GUGUDAN in text:
            print('****** 초록불 깜빡깜빡 ******')
            play_music(1)
            say("Start gugudan")

            gugudan(say, hear, success, fail)

            play_music(2)

        elif game_code.Main.DEOHAGI in text:
            print('****** 보라색 불 깜빡깜빡 ******')
            play_music(1)
            say("Start deohagi")

            deohagi(say, hear, success, fail)

            play_music(2)
        elif game_code.Main.UPDOWN in text:
            print('****** 노란색 불 깜빡깜빡 ******')
            play_music(1)
            say("Start updown")

            updown(say, hear, success, fail)

            play_music(2)

        elif dust_code.Main.NAME in text:
            def turn_on(color):
                print('****** {} 불 깜빡깜빡 ******'.format(color))

            def turn_off():
                print('------ 불 꺼짐 ------')

            dust(text, say, turn_on, turn_off)

        # 끝내기
        elif check_word(text, game_code.Main.END):
            break

        # 그 외의 것 말함 (없는 명령어)
        else:
            play_music(3)


if __name__ == '__main__':
    main()
