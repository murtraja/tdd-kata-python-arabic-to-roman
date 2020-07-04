from collections import OrderedDict
literal_map = OrderedDict({
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
})

def convert(arabic):
    if arabic in literal_map:
        return literal_map[arabic]
    lo, hi = get_bounds(arabic)
    print(f'{lo} {arabic} {hi}')

    subtraction = subtraction_case(arabic, hi)
    if lo != hi and subtraction:
        return subtraction
    else:
        return addition_case(arabic, lo)

# def is_subtraction_case(arabic, hi):
#     '''
#     IV V diff 1 => 1/5 = 0.2
#     IX X diff 1 => 1/10 = 0.1
#     VIII X diff 2 => 2/10 = 0.2
#     '''
#     diff = hi-arabic
#     if diff in literal_map:
#         return True

def subtraction_case(arabic, hi):
    keys = get_ordered_key_list()
    hi_index = keys.index(hi)
    lo_index = hi_index - 1
    allowed_subtraction_index = lo_index - lo_index%2
    allowed_subtraction_value = keys[allowed_subtraction_index]
    diff = hi-arabic
    if diff > allowed_subtraction_value:
        return False
    diff_mapped = literal_map[allowed_subtraction_value]
    return diff_mapped + literal_map[hi] + convert(allowed_subtraction_value-diff)

def addition_case(arabic, lo):
    return convert_quotient(arabic, lo) + \
        convert_remainder(arabic, lo)

def convert_quotient(arabic, lo):
    return literal_map[lo]*(arabic//lo)

def convert_remainder(arabic, lo):
    rem = arabic%lo
    rem_roman = ''
    if rem != 0:
        return convert(rem)
    return ''

def get_ordered_key_list():
    return list(literal_map.keys())

def get_bounds(arabic):
    keys = get_ordered_key_list()
    for i in range(len(keys)-1):
        lower = keys[i]
        upper = keys[i+1]
        if arabic > lower and arabic < upper:
            return (lower, upper)
    return (upper, upper)