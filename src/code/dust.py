
class State:
    SEOUL = ('서울')
    JEJU = ('제주')

    list = {
        'seoul': SEOUL,
        'jeju': JEJU
    }


class Level:
    GOOD = 0
    AVERAGE = 1
    BAD = 2
    VERY_BAD = 3

    list = ('Very Good', 'So so', 'Bad', 'Very Bad')


class Color:
    BLUE   = (0x00, 0x00, 0xFF)
    GREEN  = (0x00, 0xFF, 0x00)
    YELLOW = (0xFF, 0xFF, 0x00)
    RED    = (0xFF, 0x00, 0x00)

    GOOD = BLUE
    AVERAGE = GREEN
    BAD = YELLOW
    VERY_BAD = RED

    list = (GOOD, AVERAGE, BAD, VERY_BAD)
