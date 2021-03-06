import os
import pygame
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)

file_dir = os.path.realpath(__file__)
music_dir = os.path.normpath(os.path.join(file_dir, '../../../static/music'))


def play_music(music_number):
    pygame.mixer.init()

    if music_number == 1:
        # 게임 시작할 때 -> 피카츄
        logger.info('Game Start : Pikachu!')
        pygame.mixer.music.load(os.path.join(music_dir, 'pikachu.mp3'))
        pygame.mixer.music.play(0)

    elif music_number == 2:
        # 게임 끝날 때 -> 피카피피카츄
        logger.info('Game Finished : Pikapi-Pikachu!')
        print(os.path.join(music_dir, 'pikapi_pikachu.mp3'))
        pygame.mixer.music.load(os.path.join(music_dir, 'pikapi_pikachu.mp3'))
        pygame.mixer.music.play(0)

    elif music_number == 3:
        # 못 알아 들었을 때 -> 피카피카
        logger.info('Unknown Command : Pika-Pika!')
        pygame.mixer.music.load(os.path.join(music_dir, 'pika_pika.mp3'))
        pygame.mixer.music.play(0)

    else:
        logger.info('Wrong music number')

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.quit()

    
