options = [['12', '1+2', '1-2'],
           ['3', '+3', '-3'],
           ['4', '+4', '-4'],
           ['5', '+5', '-5'],
           ['6', '+6', '-6'],
           ['7', '+7', '-7'],
           ['8', '+8', '-8'],
           ['9', '+9', '-9']]


def get_products(l_a, l_b):
    result = []

    for a in l_a:
        for b in l_b:
            result.append(a + b)

    return result

while len(options) > 1:
    args = options[:2]

    products = get_products(*args)

    for arg in args:
        options.remove(arg)

    options.append(products)

variations = options[0]
correct = []

for variation in variations:
    if eval(variation) == 100:
        correct.append(variation)

print(correct)