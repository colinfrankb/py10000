#!/usr/bin/env python

def decimal_to_roman_numeral(decimal):
    string_decimal = str(decimal)
    mapping = [
        ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['', 'M']
    ]

    result = []
    for i in range(0, len(string_decimal)):

        string_index = len(string_decimal) - 1 - i

        result.insert(0, mapping[i][int(string_decimal[string_index])])

    return ''.join(result)


def test_decimal_to_roman_numeral():

    print(decimal_to_roman_numeral(4) == 'IV')
    print(decimal_to_roman_numeral(41) == 'XLI')
    print(decimal_to_roman_numeral(10) == 'X')
    print(decimal_to_roman_numeral(9) == 'IX')
    print(decimal_to_roman_numeral(112) == 'CXII')
    print(decimal_to_roman_numeral(999) == 'CMXCIX')
    print(decimal_to_roman_numeral(1000) == 'M')


test_decimal_to_roman_numeral()