'''
If you haven't gathered from the title, the challenge here is to go from
decimal notation -> scientific notation. For those that don't know,
scientific notation allows for a decimal less than ten, greater than
zero, and a power of ten to be multiplied.

For example: 239487 would be 2.39487 x 105

And .654 would be 6.54 x 10-1

Bonus Points:

    Have you program randomly generate the number that you will translate.

    Go both ways (i.e., given 0.935 x 103, output 935.)

Good luck, and have fun!
'''

def sign(s):
    negative = re.findall('-', s)
    if not negative:
        negative = ''
    else:
        negative = negative[0]
    return negative


def zero_cull(s):
    '''cull leading zeros'''
    if ',' in s:
        s = re.sub("\.|0+", "", s)
    else:
        s = re.sub('^0+', '', s)
    return s


def leading_digit(s):
    digit = re.findall('([1-9])', s)
    if digit == []:
        digit = 0
    else:
        digit = digit[0]
    return digit

def remainder_(s):
    remainder = re.findall('[\d](\d+)', s)
    if remainder == []:
        return ''
    return remainder[0]


def post_period_(s):
    if '.' in s:
        post_period = re.findall('([1-9]\d+)', s)
        post_period = post_period[0][1:]
    else:
        post_period = ''
    return post_period


def length_post_period(s):
    len_post_period = len(post_period)

    return len_post_period


def pre_period_(s):
    pre_period = re.findall('(\d+)[\.]', s)
    return pre_period


def length_pre_period(s):
    len_pre_period = len(pre_period_(s))
    return len_pre_period


def dec_1st_digit(s):
    ''' pull out the first value of
    a decimal value '''
    decimal_first_digit = re.findall('(^\d?)', s)
    decimal_first_digit = decimal_first_digit[0]
    return decimal_first_digit


def cull_trail_zeros(s):
    s = re.sub("0*$", "", s)
    return s


def calc_power(s):
    '''calc the power
    of a decimal'''
    accum = 1
    for digit in s:
        if  digit == '.':
            continue
        elif digit == '0':
            accum += 1
            continue
        else:
            return accum


if __name__ == '__main__':
    import re

    s = '0'
    s = zero_cull(s)
    sign = sign(s)
    leading_digit = leading_digit(s)
    remainder = remainder_(s)
    post_period = post_period_(s)
    len_post_period = length_post_period(s)
    pre_period = pre_period_(s)
    len_pre_period = length_pre_period(s)


    if pre_period == []:
        if '.' not in s:
            len_post_period = len(remainder)
            post_period = remainder
            digit = leading_digit
            post_period = cull_trail_zeros(post_period)
        elif '.' in s:
            digit = leading_digit
            post_period = cull_trail_zeros(post_period)
            len_post_period = '-' + str(calc_power(s))

        else:
            len_post_period = '-1'

    if leading_digit == '':
        remainder = post_period

if post_period == '':
    print('{0}{1}{2}{3}{4}{5}'.format(sign, digit, '', post_period, ' x 10^', len_post_period))
else:
    print('{0}{1}{2}{3}{4}{5}'.format(sign, digit, '.', post_period, ' x 10^', len_post_period))