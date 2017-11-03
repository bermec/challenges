'''
You work for a bank, which has recently purchased an ingenious machine
to assist in reading letters and faxes sent in by branch offices.
The machine scans the paper documents, and produces a file with a
number of entries which each look like this:

    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

Each entry is 4 lines long, and each line has 27 characters. The first
3 lines of each entry contain an account number written using pipes and
underscores, and the fourth line is blank. Each account number should
have 9 digits, all of which should be in the range 0-9.

Right now you're working in the print shop and you have to take account
numbers and produce those paper documents.
Input

You'll be given a series of numbers and you have to parse them into the
previously mentioned banner format. This input...

000000000
111111111
490067715

Output

...would reveal an output that looks like this

 _  _  _  _  _  _  _  _  _
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|


 |  |  |  |  |  |  |  |  |
 |  |  |  |  |  |  |  |  |

    _  _  _  _  _  _     _
|_||_|| || ||_   |  |  ||_
'''
import itertools

one = '''
  |
  |
'''
two = ''' _
 _|
|_
'''
three = '''_
_!
_!
'''
four = '''
!_!
  !
'''
five = ''' _
!_
 _!
'''
six = '''_
!_
!_!
'''
seven = '''_
 !
 !
'''
eight = '''_
!_!
!_!
'''
nine = ''' _
!_!
 _!
'''
zero = ''' _
! !
!_!
'''



strings = list(itertools.repeat(zero, 9))
string2 = list(itertools.repeat(one, 9))
string3 = (four, nine, zero, zero, six, seven, seven, one, five)

print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len)))
                                   for x in s.split('\n')] for s in strings])], sep='\n')
print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len)))
                                   for x in s.split('\n')] for s in string2])], sep='\n')
print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len)))
                                   for x in s.split('\n')] for s in string3])], sep='\n')