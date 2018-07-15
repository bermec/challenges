''' A garland word is one that starts and ends with the same N letters in the same order,
 for some N greater than 0, but less than the length of the word. I'll call the maximum N
 for which this works the garland word's degree.
For instance, "onion" is a garland word of degree 2, because its first 2 letters "on"
are the same as its last 2 letters. The name "garland word" comes from the fact that
you can make chains of the word in this manner:

onionionionionionionionionionion...

Today's challenge is to write a function garland that, given a lowercase word,
returns the degree of the word if it's a garland word, and 0 otherwise.
'''

candidate = ''
highest_degree = 0
degree = 0
s =''
t = ''
u =''

def garland():
    ''' str -> (str,int) '''
    global candidate, highest_degree, degree, s, t, u

    # read text file of single words
    text = open('enable1.txt', 'r')
    for word in text:
        word = word.strip('\n')
        s = word

        # split into two sections and compare
        for x in range(0, len(s)):
            t = s[:x]
            u = s[-x:]

            # compare....
            if t == u:
                degree = len(t)
                if degree > highest_degree:
                    highest_degree = degree
                    candidate = s
        result = (candidate, highest_degree)
    return result

if __name__ == '__main__':
    garland = garland()
    print("The largest degree 'garland word' in the text is {0} with degree {1}"
          .format(garland[0], garland[1]))

