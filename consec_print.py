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
five = '''_
!_
_ !
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


strings = [one, two, three, four, zero]

print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings])], sep='\n')