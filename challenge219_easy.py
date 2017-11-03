''' 

It should have the following basic functionality

    Add an item to the to-do list
    Delete a selected item from the to-do list
    And obviously, print out the list so I can see what to do!

Formal Inputs & Outputs
Output description

Any output that is created should be user-friendly.
When I'm viewing my to-do list, I should be able to
easily discern one list item from another.
Examples

Input:

addItem('Take a shower');
addItem('Go to work');
viewList();

Output:

Take a shower
Go to work

Further Input:

addItem('Buy a new phone');
deleteItem('Go to work');
viewList();

Outputs:

Take a shower
Buy a new phone

'''

import collections

acc = 1
menuItems = collections.OrderedDict()

def itemIn():
    global acc
    global menuItems
    item = input('Item name?')
    added_item = menuItems[acc] = item
    acc += 1
    return menuItems

def itemOut():
    display = menu()
    delItem = input('Which item?')
    delItem = int(delItem)
    del menuItems[delItem]


def menu():
    global acc
    global menuItems
    for k, v in menuItems.items():
        print(k, v)

if __name__ == '__main__':

    ans = True
    while ans:
        print("""
        1.Add a Item
        2.Delete an Item
        3.Check List
        4.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            choice = itemIn()
            print("\n Item Added")
        elif ans == "2":
            choice = itemOut()
            print("\n Item Deleted")
        elif ans == "3":
            choice = menu()
            print("\n List Found")
        elif ans == "4":
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")