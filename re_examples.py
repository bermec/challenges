import re

wood = 'wo wood at oh at cat catch'
addr = 'You will find him at rog.pynguins.com or on facebook'

m = re.findall(r'o+', wood)
mm = re.findall(r'\scat\s', wood)
mmm = re.findall(r'cat', wood)
email = re.findall(r'\w+\.\w+\.\w+', addr)
print(m, mm, mmm)
print(email)

candidates = """2015-07-01 2015-07-04 YDM
       2016-03-01 2016-05-05 DMY
       2022-09-05 2023-09-04 YMD"""


codes = re.findall('(YMD|DMY|YDM)', candidates)
print('codes ', codes)


newstring = re.sub(r"\b","",date.strftime(z,'%m/%d/%Y'))
print('newstring: 2013-12-4 ', newstring)


lst = ' 2012 5 8'
year = re.findall('[^\s]\d+', lst)
year2 = re.findall('\d+', lst)

print(year)
print(year2)

