'''


As an optional bonus, decrypt the following message, which has been
encrypted with a word that I've used in this post:

HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLN
BASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABB
AISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISY
MAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR

'''

def decode(coded, code_lst):
    ans = ''
    accum = 0
    flag = 0
    while accum < len(coded):
        for x in range(0, len(coded)):
            flag = 0
            ordN = ord(coded[x])
            for the_code in trimmed_list[x]:
                if flag == 1:
                    break
                ordG = ord(the_code)
                for x in range(0, 91):
                    if (ordG + x) % 26 + 65 == ordN:
                        if chr(x).isalpha():
                            ans += (chr(x))
                            accum += 1
                            flag = 1
                            break
    return ans


if __name__ =='__main__':

    coded = '''HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLN
    BASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABB
    AISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISY
    MAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR'''
    code = list('BEGINNING' * len(coded))
    # cut code to the required length
    trimmed_list = code[0: len(coded)]
    code_lst = list(trimmed_list)

    ans = decode(coded, code_lst)
    print(ans)
