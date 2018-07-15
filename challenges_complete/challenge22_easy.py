''' Write a program that will compare two lists, and append any elements in the
second list that doesn't exist in the first.

input: ["a","b","c",1,4,], ["a", "x", 34, "4"]

output: ["a", "b", "c",1,4,"x",34, "4"]

'''

list1 = ["a", "b", "c", 1, 4 ]
list2 = ["a", "x", 34, "4"]

for x in list2:
    if x not in list1:
        list1.append(x)

print(list1)

