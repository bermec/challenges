''' In this challenge, we are going to take a sentence and mangle it up by sorting
the letters in each word. So, for instance, if you take the word "hello" and sort
the letters in it, you get "ehllo". If you take the two words "hello world", and
sort the letters in each word, you get "ehllo dlorw".
Inputs & outputs
Input

The input will be a single line that is exactly one English sentence,
starting with a capital letter and ending with a period
Output

The output will be the same sentence with all the letters in each word sorted.
Words that were capitalized in the input needs to be capitalized properly in
the output, and any punctuation should remain at the same place as it started.
So, for instance, "Dailyprogrammer" should become "Aadegilmmoprrry" (note
the capital A), and "doesn't" should become "denos't".

To be clear, only spaces separate words, not any other kind of punctuation.
So "time-worn" should be transformed into "eimn-ortw", not "eimt-norw", and
"Mickey's" should be transformed into "Ceikms'y", not anything else.

Edit: It has been pointed out to me that this criterion might make the problem
a bit too difficult for [easy] difficulty. If you find this version too challenging,
you can consider every non-alphabetic character as splitting a word. So "time-worn"
becomes "eimt-norw" and "Mickey's" becomes ""Ceikmy's". Consider the harder version as a Bonus.
'''
def jumble(words):
    outstring = ''
    output = ''
    words = words.split()

    for word in words:
        outstring = ''
        # collect alpha characters from string 'word'
        d = ''
        for char in word:
            if char.isalpha():
                d += char

        # sort the letters (d), lower b4 sorting
        d = d.lower()
        d = sorted(d)
        d = ''.join(d)

        # replace the sorted string
        y = 0
        for x in range(0, len(word)):
            if word[x].isalpha():
                temp = word[x]
                temp2 = temp.replace(temp, d[y])
                outstring += temp2
                y += 1
            else:
                temp = word[x]
                outstring += temp
        outstring += ' '


        # replace capital letter
        # check index of the capital letter if any, 'cap_index'.
        for index, char in enumerate(word):
            if char.isupper():
                cap_index = index
                # replace the upper case
                upperCase = outstring[cap_index].upper()
                outstring = outstring. replace(outstring[cap_index], upperCase)
        output += outstring

    return output






if __name__ == '__main__':
    sentence = "For others in al-Wair, it's the only way forward to begin to end a devastating " \
          "war and to ease the suffering of civilians who have paid a heavy price."
    #sentence = " al-Wair, it's done."
    ans = jumble(sentence)
    print(ans)

