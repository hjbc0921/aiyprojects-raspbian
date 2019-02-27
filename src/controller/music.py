import pygame
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)


def play_music(music_number):
    pygame.init()

    if music_number == 1:
        # 게임 시작할 때 -> 피카츄
        logger.info('Game Start : Pikachu!')
        pygame.mixer.music.load("pikachu.mp3")
        pygame.mixer.music.play(0)

    elif music_number == 2:
        # 게임 끝날 때 -> 피카피피카츄
        logger.info('Game Finished : Pikapi-Pikachu!')
        pygame.mixer.music.load("pikapi_pikachu.mp3")
        pygame.mixer.music.play(0)

    elif music_number == 3:
        # 못 알아 들었을 때 -> 피카피카
        logger.info('Unknown Command : Pika-Pika!')
        pygame.mixer.music.load("pika_pika.mp3")
        pygame.mixer.music.play(0)

    else:
        logger.info('Wrong music number')

    pygame.quit()
