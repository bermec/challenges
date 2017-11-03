'''
retrieve key from known value
value must be unique
'''

countries = {'uk':'1'}

for k, v in countries.items():
    if "1" == v or isinstance(v, list) and "1" in v:
        print(k)