
def dec_to_hex(n):
    hex_num = {10: 'A',
               11: 'B',
               12: 'C',
               13:'D',
               14: 'C',
               15: 'D'}
    hex_list = []
    while True:
        num = n // 16
        if num > 9:
            numb = hex_num[num]
        hex_list.append(numb)
        n = n - (num * 16)
        pass
        if n > 9:
            n = hex_num[n]
        hex_list.append(n)
        hex_string = ''
        for char in hex_list:
            hex_string += str(char)
        break
    return hex_string


ans = dec_to_hex(211)
print(ans)