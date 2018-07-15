'''
You have just been hired at a local home improvement store to help compute the proper
costs of inventory. The current prices are out of date and wrong; you have to figure
out which items need to be re-labeled with the correct price.

You will be first given a list of item-names and their current price. You will then be
given another list of the same item-names but with the correct price. You must then
print a list of items that have changed, and by how much.
Formal Inputs & Outputs
Input Description

The first line of input will be an integer N, which is for the number of rows in each
list. Each list has N-lines of two space-delimited strings: the first string will be the
unique item name (without spaces), the second string will be the price (in whole-integer
cents). The second list, following the same format, will have the same unique item-names,
but with the correct price. Note that the lists may not be in the same order!
Output Description

For each item that has had its price changed, print a row with the item name and the price
difference (in cents). Print the sign of the change (e.g. '+' for a growth in price, or '-'
for a loss in price). Order does not matter for output.
Sample Inputs & Outputs
Sample Input 1

4
CarriageBolt 45
Eyebolt 50
Washer 120
Rivet 10
CarriageBolt 45
Eyebolt 45
Washer 140
Rivet 10

Sample Output 1

Eyebolt -5
Washer +20

Sample Input 2

3
2DNail 3
4DNail 5
8DNail 10
8DNail 11
4DNail 5
2DNail 2

Sample Output 2

2DNail -1
8DNail +1

'''
import re

def stock_update(s, N):
    names = re.findall('\d[a-zA-Z]+\s\d+|[a-zA-Z]+\s\d+', s)
    # print(names)
    old_items = []
    for x in range(0, N):
        item = names[x]
        old_items.append(item)

    present_items = []
    for x in range(0 + N, N + N):
        item = names[x]
        present_items.append(item)

    old_items = sorted(old_items)
    present_items = sorted(present_items)

    old_items = ','.join(old_items)
    present_items = ','.join(present_items)

    old_prices = re.findall('\s(\d+)', old_items)
    present_prices = re.findall('\s(\d+)', present_items)

    goods = re.findall('\d+[a-zA-Z]+|[a-zA-Z]+', old_items)

    changed_stock = []
    for x in range(0, N):
        diff = int(present_prices[x]) - int(old_prices[x])
        if diff != 0:
            if diff > 0:
                changed_stock.append(goods[x] + ' +' + str(diff))
            else:
                changed_stock.append(goods[x] + ' ' + str(diff))
    return changed_stock

if __name__ == '__main__':

    stock = '''CarriageBolt 45
    Eyebolt 50
    Washer 120
    Rivet 10
    CarriageBolt 45
    Eyebolt 45
    Washer 140
    Rivet 10'''

    N = 4

    stock_updated = stock_update(stock, N)
    for item in stock_updated:
        print(item)
    print()

    stock2 = '''2DNail 3
    4DNail 5
    8DNail 10
    8DNail 11
    4DNail 5
    2DNail 2'''

    N = 3

    stock_updated = stock_update(stock2, N)
    for item in stock_updated:
        print(item)

