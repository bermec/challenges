'''
The world's most prestigious art gallery in the world needs your help!
Management wants to figure out how many people visit each room in the
gallery, and for how long: this is to help improve the quality of the
overall gallery in the future.

Your goal is to write a program that takes a formatted log file that
describes the overall gallery's foot-traffic on a minute-to-minute basis.
From this data you must compute the average time spent in each room, and
how many visitors there were in each room.

Author: nint22
Formal Inputs & Outputs
Input Description

You will be first given an integer N which represents the following
N-number of lines of text. Each line represents either a visitor entering
or leaving a room: it starts with an integer, representing a visitor's
unique identifier. Next on this line is another integer, representing the
 index. Note that there are at most 100 rooms, starting at index 0, and at
 most 1,024 visitors, starting at index 0. Next is a single character,
 either 'I' (for "In") for this visitor entering the room, or 'O' (for "out")
 for the visitor leaving the room. Finally, at the end of this line, there
 is a time-stamp integer: it is an integer representing the minute the event
 occurred during the day. This integer will range from 0 to 1439 (inclusive).
 All of these elements are space-delimited.

You may assume that all input is logically well-formed: for each person
entering a room, he or she will always leave it at some point in the future.
A visitor will only be in one room at a time.

Note that the order of events in the log are not sorted in any way; it
shouldn't matter, as you can solve this problem without sorting given data.
Your output (see details below) must be sorted by room index, ascending.
Output Description

For each room that had log data associated with it, print the room index
(starting at 0), then print the average length of time visitors have stayed
as an integer (round down), and then finally print the total number of visitors
in the room. All of this should be on the same line and be space delimited;
you may optionally include labels on this text, like in our sample output 1.
Sample Inputs & Outputs
Sample Input 1

4
0 0 I 540
1 0 I 540
0 0 O 560
1 0 O 560

Sample Output 1

Room 0, 20 minute average visit, 2 visitor(s) total

Sample Input 2

36
0 11 I 347
7 11 O 418
8 1 O 418
0 12 I 437
1 28 I 343
2 32 I 408
3 15 I 458
4 18 I 424
5 26 I 442
6 7 I 435
7 19 I 456
8 19 I 450
0 12 O 455
1 28 O 374
2 32 O 495
3 15 O 462
4 18 O 500
5 26 O 479
6 7 O 493
7 19 O 471
8 19 O 458
1 13 I 307
2 15 I 334
3 6 I 334
4 9 I 334
5 2 I 334
6 2 I 334
7 11 I 334
8 1 I 334
0 11 O 376
1 13 O 321
2 15 O 389
3 6 O 412
4 9 O 418
5 2 O 414
6 2 O 349


Sample Output 2

Room 1, 85 minute average visit, 1 visitor total
Room 2, 48 minute average visit, 2 visitors total
Room 6, 79 minute average visit, 1 visitor total
Room 7, 59 minute average visit, 1 visitor total
Room 9, 85 minute average visit, 1 visitor total
Room 11, 57 minute average visit, 2 visitors total
Room 12, 19 minute average visit, 1 visitor total
Room 13, 15 minute average visit, 1 visitor total
Room 15, 30 minute average visit, 2 visitors total
Room 18, 77 minute average visit, 1 visitor total
Room 19, 12 minute average visit, 2 visitors total
Room 26, 38 minute average visit, 1 visitor total
Room 28, 32 minute average visit, 1 visitor total
Room 32, 88 minute average visit, 1 visitor total

'''
import collections
import re
room_visits = {}
room_visitor_length = {}
visitor_in = 'I'
visitor_out = 'O'


def sort_human(l):
    convert = lambda text: float(text) if text.isdigit() else text
    alphanum = lambda key: [ convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]+)', key) ]
    l.sort( key=alphanum )
    return l


candidates = '''0 11 I 347
7 11 O 418
8 1 O 418
0 12 I 437
1 28 I 343
2 32 I 408
3 15 I 458
4 18 I 424
5 26 I 442
6 7 I 435
7 19 I 456
8 19 I 450
0 12 O 455
1 28 O 374
2 32 O 495
3 15 O 462
4 18 O 500
5 26 O 479
6 7 O 493
7 19 O 471
8 19 O 458
1 13 I 307
2 15 I 334
3 6 I 334
4 9 I 334
5 2 I 334
6 2 I 334
7 11 I 334
8 1 I 334
0 11 O 376
1 13 O 321
2 15 O 389
3 6 O 412
4 9 O 418
5 2 O 414
6 2 O 349'''

# check room visits, place room and visits in a dictionary
candidates = candidates.split('\n')
for candidate in candidates:
    candidate = candidate.split()
    # visitor in.
    if candidate[2] == visitor_in:
        # room number and visit count.
        room_visits[candidate[1]] = room_visits.get(candidate[1], 0) + 1

room_visit_list = []
for k,v in room_visits.items():
    room_visit_list.append(v)

time_in_room = {}
# calc time in room
for candidate in candidates:
    if candidate == '':
        continue
    candidate = candidate.split()
    if len(candidate) > 0:
        pass
    else:
        continue
    # if visitor goes in room
    if candidate[2] == visitor_in:
        in_time = candidate[3]
        visitor = candidate[0]
        the_room = candidate[1]

        # check when visitor leaves room
        for x in range(0, len(candidates)):
            temp = candidates[x]
            candidate = temp.split()
            if len(candidate) > 0:
                pass
            else:
                continue
            if (candidate[0] == visitor) and (candidate[2] == visitor_out) and (candidate[1] == the_room):
                out_time = candidate[3]
                visitor_time = float(out_time) - float(in_time)
                room_visitor_length[the_room] = room_visitor_length.get(the_room, 0) + visitor_time
                candidates[x] = ''
                break

visitor_length = []
for k,v in room_visitor_length.items():
    visitor_length.append(v)


room_list = []
for k,v in room_visits.items():
    room_list.append(k)

# iterate for printing
output_list =[]

for x in range(0, len(room_visits)):
    room = room_list[x]
    visits = room_visit_list[x]
    visit_length = visitor_length[x]
    average_time = int(visit_length / visits)
    output_list.append('Room ' + room + ', ' + str(int(average_time)) +
          ' minute average visit, ' + str(visits) + ' visitor total')


output_list = sort_human(output_list)
for text in output_list:
    print(text)

