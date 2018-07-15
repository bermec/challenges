import re
formula = '+4x^3 -0x^2 -6x^1 +7'
co_effs = re.findall('[+-]\d+', formula)
co_exps = re.findall('[\^](\d+)', formula)
co_exps.append('0')
print(co_effs)
print(co_exps)
multiplier = '4x^2'
coeff_mult = re.findall('^\d+', multiplier)
coexp_mult = re.findall('\d+$', multiplier)
print(coeff_mult, coexp_mult)