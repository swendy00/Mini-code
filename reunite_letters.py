import json
import copy

basic_map = {
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


# reunite letters
def reunite(a, b):
    result = []
    if not isinstance(a, list) or not isinstance(b, list):
        return
    for i in a:
        for k in b:
            result.append(i + k)
    return result


def stage1_test(letter_map):

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
        for k in keys:
            if str(k) in letter_map.keys() and letter_map[str(k)]:
                action_letters.append(letter_map[str(k)])

        # reunite action letters
        if len(action_letters) > 0:
            result = action_letters[0]
            for i in range(1, len(action_letters)):
                result = reunite(result, action_letters[i])

            print("Output: ", end='')
            for i in result:
                print(i, end=' ')
            return result
        else:
            print("Output: ", end='')
    except Exception:
        print("Input Error : %s ." % "please input a 'list' like the example above, all objects in the list must be an integer")
    finally:
        pass


def stage2_test(letter_map):
    new_letter_map = copy.deepcopy(letter_map)

    # create a new map, add digits from 10 to 99 to the new map.
    for i in range(len(basic_map), 100):
        new_letter_map.setdefault(str(i), [])

    stage1_test(new_letter_map)


if __name__ == '__main__':
    stage1_test(basic_map)
    # stage2_test(basic_map)
