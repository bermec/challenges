lst =[[1, 1, 2, 2,]]

from itertools import chain
str = '0. 0.0.'
str1 = '0 0.00.'
str2 = '.. ..0.'
zipped = zip(str, str1, str2)
#zipped =''.join(chain(*zip(str1[0::2], str[0::2])))
zipped = list(zipped)
print(zipped)
str = str.join(str)
str4 = ''
print('str: ', str)

# now flatten

zipped = sum(zipped, ())
print(zipped)