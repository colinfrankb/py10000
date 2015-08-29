l = [1, 2, 3, 4, 5, 6]


def get_sum_using_loop(l):
    result = 0

    for x in l:
        result += x

    return result

def get_sum_using_while(l):
    i = 0
    result = 0

    while(i < len(l)):
        result += l[i]
        i += 1

    return result


def get_sum_using_resursion(l):

    def loop(i, lis):
        if i + 1 < len(lis):
            return lis[i] + loop(i + 1, lis)

        return lis[i]

    return loop(0, l)


print(get_sum_using_loop(l))
print(get_sum_using_while(l))
print(get_sum_using_resursion(l))


def combine_lists(list_a, list_b):
    highest_len = max(len(list_a), len(list_b))
    result = []
    for i in range(highest_len):
        if i < len(list_a):
            result.append(list_a[i])

        if i < len(list_b):
            result.append(list_b[i])

    return result

print(combine_lists(['a', 'b', 'c'], [1, 2, 3, 4, 5]))


def largest_number(l):
    s_l = map(lambda x: str(x), l)

    return ''.join(sorted(s_l, reverse=True))

print(largest_number([50, 2, 1, 9]))
