import json


def reunite(a, b):
    result = []
    if not isinstance(a, list) or not isinstance(b, list):
        return
    for i in a:
        for k in b:
            result.append(i + k)
    return result


def test1():
    letter_map = {
        '0': [],
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    print('good example: [2,3]')
    digits = input("Input: ")

    try:
        keys = json.loads(digits)
        # check input data
        if not isinstance(keys, list):
            return "Error: input error"
        for k in keys:
            if not isinstance(k, int):
                return "Error: input error"
        # get action letters
        action_letters = []
        for i in keys:
            if str(i) in letter_map.keys() and letter_map[str(i)]:
                action_letters.append(letter_map[str(i)])
        # reunite action letters
        result = action_letters[0]
        for i in range(1, len(action_letters)):
            result = reunite(result, action_letters[i])

        print("Output: ", end='')
        for i in result:
            print(i, end=' ')

        return result

    except Exception as e:
        print("Input Error : %s ." % e)
    finally:
        pass


# def test2():
#     print(ord('!'))
#     for i in range(0, 100):
#         print(chr(i), end=' ')
#     print()


if __name__ == '__main__':
    test1()
