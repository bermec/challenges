''' write a program that will allow the user to input digits, and arrange them in numerical order.

for extra credit, have it also arrange strings in alphabetical order

'''

alpha_list = []
number_list = []

while True:
    stuff = input('Enter stuff, string or number, period to quit.')



    if str.isalpha(stuff):
        alpha_list.append(stuff)
    elif str.isdigit(stuff):
        number_list.append(stuff)
    else:
        stuff == '.'
        print(sorted(alpha_list))
        print(sorted(number_list))
        exit()


