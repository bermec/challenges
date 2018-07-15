
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


def quotient(a, b, c, d):
    q = str(int(a / b)) + 'x^' + str(c - d)
    return q


quotient_string = ''

c = '+4x^3 +2x^2 -6x +3'  # dividend

# find co-efficients and exponents in the dividend
co_effs = re.findall('([+-]\d+)+', c)
co_effs_one = int(co_effs[0])    # 4
co_effs_two = int(co_effs[1])    # 2
co_effs_three = int(co_effs[2])  # -6
co_effs_four = int(co_effs[3])   # 3

powers = re.findall('\^(\d+)', c)
if not '1' in powers:
    powers.append('1')
print('powers: ', powers)
exp_one = int(powers[0])    # 3
exp_two = int(powers[1])    # 2
exp_three = int(powers[2])  # 1

divisor = 'x - 3'

# find co-efficients and exponents in the divisor
divisor_co_eff_one = re.findall('^\d+', divisor)
if len(divisor_co_eff_one) == 0:
    divisor_co_eff_one.append('1')
divisor_co_eff_one = int(divisor_co_eff_one[0])   # 1

divisor_co_eff_two = re.findall('\s([+-]|\d)', divisor)
divisor_co_eff_two = int(divisor_co_eff_two[0] + divisor_co_eff_two[1])  # -3

divisor_exp_one = re.findall('\d+(?=x)', divisor)
if len(divisor_exp_one) == 0:
    divisor_exp_one.append('1')
divisor_exp_one = int(divisor_exp_one[0])   # 1
# ----------------------------------------------

quotient_one = quotient(co_effs_one, divisor_co_eff_one, exp_one, divisor_exp_one)
# str(int(co_effs_one / divisor_co_eff_one)) + 'x^' + str(exp_one - divisor_exp_one) # 4x^2
print('answer_one:  ',  quotient_one)

quotient_string += quotient_one

mult = multipl(quotient_one, divisor)

divisor_exp_one = re.findall('\^(\d+)', mult)
divisor_exp_one = int(divisor_exp_one[0])        # 2

divisor_co_eff_one = re.findall('[+-]\d+(?=x)', mult)
if len(divisor_co_eff_one) == 0:
    divisor_co_eff_one.append('1')
divisor_co_eff_one = int(divisor_co_eff_one[0])     # -12

quotient2 = str(co_effs_two - divisor_co_eff_one) + 'x^' + str(divisor_exp_one - 1)# 14x^1

if (co_effs_two - divisor_co_eff_one) % 2 == 0:
    quotient2_str = ' + ' + quotient2
print('quotient2: ', quotient2_str)


quotient_string += quotient2_str
print(quotient_string)

mult = multipl(quotient2, divisor)    # 14x^1, x - 3
print(mult)      # -42x^1

# quotient3  -----------------------------------

mult_co_effs = re.findall('[+-]\d+(?=x)', mult)
mult_co_effs = int(mult_co_effs[0])
quotient3 = co_effs_three - mult_co_effs

if quotient3 % 2 == 0:
    quotient3 = '+ ' + str(quotient3)

print(quotient3)

quotient_string += ' ' + quotient3
print(quotient_string)


# multiply quotient3 by first term of the divider

quotient3_exponent = re.findall('\d+$', quotient3)
quotient3_exponent = int(quotient3_exponent[0]) - 1

co_effs_q4 = re.findall('^[+-]\d+|\d+', quotient3)
co_effs_q4 = int(co_effs_q4[0])
mult = multipl(str(co_effs_q4), divisor)
print(mult)

quotient_four = co_effs_four - int(mult)

print(quotient_four)

quotient_string += ' + ' + str(quotient_four) + '/' + divisor
print(quotient_string)

pass


