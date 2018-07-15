''' Challenge #19 will use The Adventures of Sherlock Holmes from Project Gutenberg.

Write a program that counts the number of alphanumeric characters there are in
The Adventures of Sherlock Holmes. Exclude the Project Gutenberg header and footer,
book title, story titles, and chapters. Post your code and the alphanumeric character count.

'''

acc = 0
with open('holmes.txt')as f:
    for line in f:
        if line.strip() == 'I.':
            break
    for line in f:
        if line.strip() == 'End of the Project Gutenberg EBook of The Adventures of Sherlock Holmes, by':
            break

        for char in line:
            if char.isalnum():
                acc += 1

print(acc)