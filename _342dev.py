'''
Today's challenge is to divide two polynomials. For example,
long division can be implemented.

Display the quotient and remainder obtained upon division.
Input Description

Let the user enter two polynomials. Feel free to accept it as
you wish to. Divide the first polynomial by the second. For
the sake of clarity, I'm writing whole expressions in the
challenge input, but by all means, feel free to accept the
degree and all the coefficients of a polynomial.
Output Description

Display the remainder and quotient obtained.
Challenge Input

1:

    4x3 + 2x2 - 6x + 3

    x - 3

2:

    2x4 - 9x3 + 21x2 - 26x + 12

    2x - 3

3:

    10x4 - 7x2 -1

    x2 - x + 3

Challenge Output

1:

    Quotient: 4x2 + 14x + 36 Remainder: 111

2:

    Quotient: x3 - 3x2 +6x - 4 Remainder: 0

3:

    Quotient: 10x2 + 10x - 27 Remainder: -57x + 80

'''


import re
def multipl(s1, s2):
    # co-efficient of quotient
    a = re.findall('^[+-]\d+|^\d+', s1)
    # exponent parts of divisor
    b = re.findall('[+-]|\d+$|\d+$', s2)
    a = int(a[0])
    b = int(b[0] + b[1])
    # tail of dividend
    e = re.findall('\S\^\d+', s1)
    if e == []:
        e = ['']
    ans = str(a * b) + e[0]
    return ans


def quotient(a, b):
    co_effs_one = re.findall('^[+-]\d+', a)
    co_effs_one = int(co_effs_one[0])
    exp_one = re.findall('\^(\d+)', a)
    if not '0' in exp_one:
        exp_one.append('0')
    exp_one = int(exp_one[0])

    divisor_co_eff_one = re.findall('^\d+', b)
    if len(divisor_co_eff_one) == 0:
        divisor_co_eff_one.append('1')
    divisor_co_eff_one = int(divisor_co_eff_one[0])

    divisor_exp_one = re.findall('[\^](\d+)', b)
    if len(divisor_exp_one) == 0:
        divisor_exp_one.append('1')
    divisor_exp_one = int(divisor_exp_one[0])

    co_eff_div = str(int(co_effs_one / divisor_co_eff_one))
    if co_eff_div == '0':
        co_eff_div = '1'
    exp = exp_one - divisor_exp_one
    q = co_eff_div + 'x^' + str(exp) ##  / to -
    return q


def subtract(a, b):
    co_effs = re.findall('([+-]\d+)+', a)
    co_effs_two = int(co_effs[0])
    if str(co_effs_two) == b:
        exit()
    exp_b = re.findall('[x]\^\d+$', b)
    if exp_b == []:
        exp_b = 0
    co_eff_b = re.findall('^[+-]\d+|^\d+', b)
    try:
        co_eff_b = int(co_eff_b[0] + co_eff_b[1])
    except IndexError:
        co_eff_b = int(co_eff_b[0])
    sub = co_effs_two - co_eff_b
    return str(sub) + exp_b[0]


def division(a, b):
    co_eff_sub = re.findall('^[+-]\d+|^\d+', a)
    co_eff_sub = int(co_eff_sub[0])
    co_exp_sub = re.findall('\d+$', a)
    co_exp_sub = int(co_exp_sub[0])
    if co_exp_sub == 0:
        return ''
    tail = re.findall('[x]\^', a)
    div1 = co_eff_sub / b[0]
    div2 = co_exp_sub - b[2]
    if div2 == 0:
        return str(int(div1))
    return str(int(div1)) + tail[0] + str(div2)


def div_stats(a):
    divisor_co_eff_one = re.findall('^\d+', a)
    if len(divisor_co_eff_one) == 0:
        divisor_co_eff_one.append('1')
    divisor_co_eff_one = int(divisor_co_eff_one[0])

    divisor_co_eff_two = re.findall('\s([+-]|\d)', a)
    divisor_co_eff_two = int(divisor_co_eff_two[0] + divisor_co_eff_two[1])

    divisor_exp_one = re.findall('[\^](\d+)', a)
    if len(divisor_exp_one) == 0:
        divisor_exp_one.append('1')
    divisor_exp_one = int(divisor_exp_one[0])

    divisor_exp_two = re.findall('([\^]\d+$)', a)
    if divisor_exp_two == []:
        divisor_exp_two = 0
    else:
        divisor_exp_two = int(divisor_exp_two[0])

    a = divisor_co_eff_one
    b = divisor_co_eff_two
    c = divisor_exp_one
    d = divisor_exp_two

    return (a, b, c, d)



quotient_string = ''

#== dividend stats ==============================

dividend = '+2x^4 -9x^3 +21x^2 -26x^1 +12'  # dividend

dividends = re.findall('\S+|\S+$', dividend)

# == divisor stats =================================

divisor = '2x^1 - 3'
divstats = div_stats(divisor)

#-- quotient 1 ------------------------------------

quotient_one = quotient(dividends[0], divisor)

quotient_string += quotient_one

#-- quotient 2 -----------------------------------

mult = multipl(quotient_one, divisor)

sub = subtract(dividends[1], mult)

quotient2 = division(sub, divstats)

quotient_string += ' ' + quotient2


#-- quotient 3  -----------------------------------

mult = multipl(quotient2, divisor)

sub = subtract(dividends[2], mult)

quotient3 = division(sub, divstats)

co_eff_quotient3 = re.findall('^[-]?\d+', quotient3)
if int(co_eff_quotient3[0]) % 2 == 0:
    quotient3_str = '+ ' + str(quotient3)
quotient_string += ' ' + quotient3_str

#-- quotient 4 ------------------------------------------------

mult = multipl(quotient3, divisor)

sub = subtract(dividends[3], mult)

quotient4 = division(sub, divstats)

co_eff_quotient4 = re.findall('^[-]?\d+', quotient4)
co_eff_quotient4 = int(co_eff_quotient4[0])
if co_eff_quotient4 < 0:
    quotient4_str = ' ' + str(quotient4)
else:
    quotient4_str = ' +' + str(quotient4)
quotient_string += quotient4_str
print(quotient_string)

#-- quotient 5 ---------------------------------------

mult = multipl(quotient4, divisor)    # -3x2, 2x - 3


sub = subtract(dividends[4], mult)#  12x^2

quotient5 = division(sub, divisor_co_eff_one, divisor_exp_one)

co_eff_quotient5 = re.findall('^[-]?\d+', quotient5)
if int(co_eff_quotient5[0]) % 2 == 0:
    quotient5 = '+ ' + str(quotient5)
quotient_string += ' ' + quotient5
print(quotient_string)
