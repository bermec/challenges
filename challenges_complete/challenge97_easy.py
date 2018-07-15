'''
Write a program that concatenates all text files (*.txt)
 in a directory, numbering file names in alphabetical order.
 Print a header containing some basic information above each file.

For example, if you have a directory like this:

~/example/abc.txt
~/example/def.txt
~/example/fgh.txt

And call your program like this:

nooodl:~$ ./challenge97easy example

The output would look something like this:

=== abc.txt (200 bytes)
(contents of abc.txt)

=== def.txt (300 bytes)
(contents of def.txt)

=== ghi.txt (400 bytes)
(contents of ghi.txt)

For extra credit, add a command line option '-r' to your
program that makes it recurse into subdirectories
alphabetically, too, printing larger headers for each
subdirectory.

'''

import os
from pathlib import Path
os.chdir('txt_content')
p = Path('.')
lst = os.listdir(p)
lst = sorted(lst)

for x in range(0, len(lst)):
    with open(lst[x])as r:
        size = r.seek(0, 2)
        print('{0}{1}{2}{3}{4}'.format('=== ', lst[x],' (', size, ' bytes)'))
        print('{0}{1}{2}'.format('(contents of ', lst[x], ')'))
        print()




