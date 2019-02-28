#!/usr/bin/env python3


def text_to_number(text):
    if not text:
        return 0

    number = '영일이삼사오육칠팔구'
    unit = {'십': 10, '백': 100, '천': 1000, '만': 10000, '억': 100000000, '조': 1000000000000}

    num = tmp_result = result = 0

    for s in text:
        try:
            check = number.index(s)
        except ValueError:
            check = -1
        if check == -1:
            if unit.get(s, -1) == -1:
                return -1

            tmp_result += num
            result += (1 if tmp_result == 0 else tmp_result) * unit.get(s)
            tmp_result = 0
            num = 0
        else:
            num = check

    return result + tmp_result + num


if __name__ == '__main__':
    while True:
        print(text_to_number(input('You say:')))
