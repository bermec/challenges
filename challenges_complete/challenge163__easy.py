'''
Today's challenge we explore some curiosity in rolling a 6 sided di. I often wonder about the
outcomes of a rolling a simple 6 side di in a game or even simulating the roll on a computer.

I could roll a 6 side di and record the results. This can be time consuming, tedious and I
think it is something a computer can do very well.

So what I want to do is simulate rolling a 6 sided di in 6 groups and record how often each
number 1-6 comes up. Then print out a fancy chart comparing the data. What I want to see is if
I roll the 6 sided di more often does the results flatten out in distribution of the results or
is it very chaotic and have spikes in what numbers can come up.

So roll a D6 10, 100, 1000, 10000, 100000, 1000000 times and each time record how often a 1-6
comes up and produce a chart of % of each outcome.

Run the program one time or several times and decide for yourself. Does the results flatten out
over time? Is it always flat? Spikes can occur?
Input:

None.
Output:

Show a nicely formatted chart showing the groups of rolls and the percentages of results coming up
for human analysis.
example:

# of Rolls 1s     2s     3s     4s     5s     6s
====================================================
10         18.10% 19.20% 18.23% 20.21% 22.98% 23.20%
100        18.10% 19.20% 18.23% 20.21% 22.98% 23.20%
1000       18.10% 19.20% 18.23% 20.21% 22.98% 23.20%
10000      18.10% 19.20% 18.23% 20.21% 22.98% 23.20%
100000     18.10% 19.20% 18.23% 20.21% 22.98% 23.20%
1000000    18.10% 19.20% 18.23% 20.21% 22.98% 23.20%

notes on example output:

    Yes in the example the percentages don't add up to 100% but your results should
    Yes I used the same percentages as examples for each outcome. Results will vary.
    Your choice on how many places past the decimal you wish to show. I picked 2. if you want to show
    less/more go for it.

Code Submission + Conclusion:

Do not just post your code. Also post your conclusion based on the simulation output. Have fun and
enjoy not having to tally 1 million rolls by hand.
'''
import random

def rand_throw():
    ''' individual throw '''
    num = random.randrange(1, 7)
    return num


def rand_collection(n):
    ''' n throws '''
    lst = []
    for x in range(0, n):
        die = rand_throw()
        lst.append(die)
    return lst


def num_data(n):
    ''' sort into throw results '''
    data_list = []
    input_list = rand_collection(n)
    for x in range(1, 7):
        num = input_list.count(x)
        data_list.append((num / n) * 100)
    return data_list


if __name__ == '__main__':

    print('# of rolls 1s      2s      3s      4s      5s      6s')
    print('=' * 56)
    N_list = [10, 100, 1000, 10000, 100000, 1000000]
    for N in N_list:
        lst = num_data(N)
        lst2 = []
        for num in lst:
            num = round(num, 2)
            lst2.append(num)
        print('{:<10}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}'.format(N, lst2[0], lst2[1], lst2[2], lst2[3], lst2[4], lst2[5]))

