''' Description:

I had a dream a few weeks back that I thought would be a good challenge. I woke up early and quickly typed up a text description so I wouldn't forget (Seriously, it was about 5am and when I explained it to my wife she just laughed at me)

Okay so there is a valley. On each side you got cannons. They are firing words at each other.
In the middle of the valley the words would make contact and explode.
Similar letters from each word would cancel out. But the left over unique letters from each word
would fall to the valley and slowly fill it up.

So your challenge is to come up with the code given two words you eliminate letters in common at
a ratio of 1 for 1 and produce a set of letters that are left over from each word after colliding in mid air.
Which ever side has the most letters left over "wins". If each side donates an equal amount of letters it is a "tie".

Output:

List the extra letters left over after they collide and explode in mid air and determine which side wins or if it was a tie.
The design of the output I leave it for you to design and create.
 because cause
 hello below
 hit miss
 rekt pwn
 combo jumbo
 critical optical
 isoenzyme apoenzyme
 tribesman brainstem
 blames nimble
 yakuza wizard
 longbow blowup
'''

cannon_balls = \
'because cause\
 hello below\
 hit miss\
 rekt pwn\
 combo jumbo\
 critical optical\
 isoenzyme apoenzyme\
 tribesman brainstem\
 blames nimble\
 yakuza wizar\
 longbow blowup,'

# list of 'cannon balls'
armoury = []
cannon_balls = cannon_balls.split()

# lets give out the ammo
loony_left = []
hard_right = []

for x in range(0, len(cannon_balls)):
    if x % 2 == 0:
        loony_left.append(cannon_balls[x])
    else:
        hard_right.append(cannon_balls[x])

# load them up
for word in range(0, len(loony_left)):
    loadup = loony_left[word]
    loadup2 = hard_right[word]

    # check result of bombardment
    for char in loadup2 + loadup:
        if char in loadup and char in loadup2:
            loadup = loadup.replace(char, '')
            loadup2 = loadup2.replace(char, '')

    if len(loadup) == len(loadup2):
        print("It's a tie!")
    elif len(loadup) > len(loadup2):
        print("Loony_left wins!")
    else:
        print("Hard_right wins!")

