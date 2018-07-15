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
def multipl(s1, s2, s3):
    mult_string = ''
    # co-efficient of quotient
    if 'x' not in s1:
        coeff_q = int(s1)
    else:
        coeff_q = re.findall('^[+-]\d+|^\d+', s1)
        coeff_q = int(coeff_q[0])

    # exponent part of quotient
    exp_q = re.findall('[\^](\d+)', s1)
    if exp_q == []:
        exp_q = 0
    else:
        exp_q = int(exp_q[0])

    for x in range(0, len(s2)):
        co_ef = coeff_q * int(s2[x])
        exp = str(exp_q + int(s3[x]))
        if co_ef >= 0:
            mult_string += '+' + str(co_ef) + 'x^' + exp + ' '
        else:
            mult_string += ' ' + str(co_ef) + 'x^' + exp + ' '

    return mult_string


def quotient_is(a, b):
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

    divisor_exp = re.findall('[x^](\d+)', b)
    if len(divisor_exp) == 0:
        divisor_exp.append('1')
    divisor_exp = int(divisor_exp[0])

    co_eff_div = str(int(co_effs_one / divisor_co_eff_one))
    if co_eff_div == '0':
        co_eff_div = '1'
    exp = exp_one - divisor_exp
    q = co_eff_div + 'x^' + str(exp) ##  / to -
    return q


def trim_div(s):
    output = ''
    trim_list = re.findall('\S+', s)
    trim_list = trim_list[1:]
    for item in trim_list:
        output += item + ' '
    return output


def subtract(a, b):
    sub_output = ''
    # coefficients of the dividend
    co_effs = re.findall('([+-]\d+|\s[+-]\d+)', a)
    # exponents of the dividend
    exps = re.findall('[x]\^\d+', a)
    if len(exps) < len(co_effs):
        exps.append('x^0')
    co_eff_mult = re.findall('([+-]\d+|\s[+-]\d+)', b)
    for x in range(0, len(co_effs)):
        divi_coeff = co_effs[x]
        try:
            mult_coeff = co_eff_mult[x]
        except IndexError:
            mult_coeff = '0'
        subtracted = int(divi_coeff) - int(mult_coeff)
        try:
            if subtracted == 0:
                sub_output += ' '
            else:
                sub_output += str(subtracted) + exps[x] + ' '
        except IndexError:
            sub_output += str(subtracted)
    #output = trim_div(sub_output)

    return sub_output


def division(a, b):
    ''' divide the leading term of "a" by
    the leading term of the divisor'''
    if 'x' not in a:
        return ' ' + str(a)
    co_eff_sub = re.findall('^[+-]\d+|^\d+', a)
    co_eff_sub = int(co_eff_sub[0])
    co_exp_sub = re.findall('\^(\d+)', a)
    co_exp_sub = int(co_exp_sub[0])
    if co_exp_sub < int(b[1][0]):
        return a + '/' + divisor
    if co_exp_sub == 0:
        return ''
    tail = re.findall('[x]\^', a)
    div1 = co_eff_sub / int(b[0][0])
    div2 = co_exp_sub - int(b[1][0])
    if div2 == 0:
        return str(int(div1))
    return str(int(div1)) + tail[0] + str(div2)


def div_stats(a):
    div_coeffs = []
    # break 'a' into parts for processing
    div_parts = re.findall('\S+', a)
    # find co-efficients
    for x in range(0, len(div_parts)):
        co_eff = re.findall('^[+-]\d+|^\d+', div_parts[x])
        div_coeffs.append(co_eff[0])

    # find exponents
    div_exps = []
    # find exponents
    for x in range(0, len(div_parts)):
        exps = re.findall('\^(\d+)', div_parts[x])
        if div_parts[x].endswith('x'):
            exps = '1'
        elif '^' not in div_parts[x]:
            exps = '0'
        div_exps.append(exps[0])

    return (div_coeffs, div_exps)


if __name__ == '__main__':


    quotient_string = ''
    isnum = None

    #== dividend stats ==============================

    dividend = '+2x^4 -9x^3 +21x^2 +26x^1 +12'  # dividend
    #dividend = '+4x^3 +2x^2 -6x +3'
    #dividend = '+10x^4 +0x^3 -7x^2 +0x^1 -1'

    dividends = re.findall('\S+|\S+$', dividend)

    # == divisor stats =================================

    divisor = '2x^1 -3'
    #divisor = 'x -3'
    #divisor = '1x^2 -1x^1 +3'

    divstats = div_stats(divisor)

    for x in range(0, len(dividends)):
        if x == 0:
            quotient = quotient_is(dividends[x], divisor)
            quotient_string += quotient
        else:
            mult = multipl(quotient, divstats[0], divstats[1])
            sub = subtract(dividend, mult)
            sub_extract = re.findall('\s+', sub)
            quotient = sub_extract[0]
            dividend = sub
            quotient = division(sub, divstats)

            if isnum:
                if co_eff_quotient >= 0:
                    quotient_string += ' +' + str(sub) + '/' + divisor
                else:
                    quotient_string += '  ' + str(sub) + '/' + divisor
                break
            isnum = quotient.lstrip('+-').isdigit()

            co_eff_quotient = re.findall('^[+-]?\d+|\d+', quotient)
            try:
                co_eff_quotient = int(co_eff_quotient[0])
            except IndexError:
                quotient_int = re.findall('[+-]\d+', quotient)
                quotient_int = int(quotient_int[0])
                if quotient_int < 0:
                    quotient_string = ' ' + str(quotient)
                else:
                    quotient_string = ' +' + str(quotient)

            if co_eff_quotient < 0:
                quotient_string += ' ' + str(quotient)
            else:
                quotient_string += ' +' + str(quotient)






    print(quotient_string)
