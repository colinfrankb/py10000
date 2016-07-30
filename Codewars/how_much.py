# def howmuch(*args):
#     m, n = sorted(args)
#     results = []
#
#     if m < 0 or n < 0 or m >= n:
#         return results
#
#     for z in range(m, n + 1):
#         c = (z - 1) / float(9)
#         b = (z - 2) / float(7)
#         if (c > 0 and c % 1 == 0) and (b > 0 and b % 1 == 0):
#             results.append(['M: {0}'.format(z), 'B: {0}'.format(int(b)), 'C: {0}'.format(int(c))])
#
#     return results


def howmuch(m, n):
    m, n = sorted([m, n])
    return [
        ['M: {}'.format(x), 'B: {}'.format(x // 7), 'C: {}'.format(x // 9)]
        for x in range(-((m - 37) // -63) * 63 + 37, n + 1, 63)]


def assert_equals(*args):
    print(args[0] == args[1])

assert_equals(howmuch(1, 100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
assert_equals(howmuch(2950, 2950), [])
assert_equals(howmuch(20000, 20100), [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]])
assert_equals(howmuch(10000, 9950), [['M: 9991', 'B: 1427', 'C: 1110']])
