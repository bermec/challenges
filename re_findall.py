import re

text = ' Roger Ward, ex Royal Engineers sat on a locomotive in the yard, he found number 730004 steaming. rog@pynguins.com'
text2 = '2d40'
text3 = '40^4'

ans = re.findall('\d+\s\w+\.', text)
ans2 = re.findall('\w+\@\w+\.\w+', text)
ans3 = re.findall('\ex', text)
ans4 = re.findall('\d{1,9}', text2)
ans5 = re.findall('\d$', text2)
ans6 = re.findall('([^\^]+)', text3)
ans7 = re.findall('(.*)\^', text3)
ans8 = re.findall('\^(.*)', text3)

print(ans)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
print(ans6)
print(ans7)
print(ans8)
