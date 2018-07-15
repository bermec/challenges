'''
Many Unix-based systems support the concept of a symbolic link. This is where one directory name is
 transparently mapped to another. Before we look further at symbolic links, here's a brief primer on Unix paths.

    The root directory on a file-system is /. Everything is contained with in /. This is like C:\ on Windows,
     but contains everything rather than just the system drive. Thus, all absolute paths begin with
    a / - if it doesn't, the path is assumed to be relative to the current location.

    Successive nested directorys are joined with slashes, so a directory a in a directory b in a directory c
    in root is denoted /c/b/a.

    To distinguish a directory from a file, a trailing slash can be added, so /c/b/a and /c/b/a/ are equivalent
    assuming a is a directory and not a file.

    Path names are case sensitive. /bin/thing is different from /bin/Thing.

Now, symbolic links are the more general equivalent of Windows shortcuts. They can be used to 'redirect'
one directory to another. For example, if I have a version of a program thing located at /bin/thing-2,
then when thing upgrades to thing 3 then any programs referring to /bin/thing-2 will break once it changes to
/bin/thing-3. Thus, I might make a symbolic link /bin/thing which refers to /bin/thing-2. This means any attempt
to visit a path beginning with /bin/thing will be silently redirected to /bin/thing-2. Hence, once the program
updates, just change the symbolic link and everything is working still.

Symbolic links can have more to them, and you can in fact make them on Windows with some NTFS trickery,
but this challenge focuses just on Unix style directories.

Our challenge is to resolve a given path name into its actual location given a number of symbolic links.
Assume that symbolic links can point to other links.

Input Description

You will accept a number N. You will then accept N lines in the format:

/path/of/link:/path/of/destination

Then you will accept a path of a directory to be fully expanded.

For example:

4
/bin/thing:/bin/thing-3
/bin/thing-3:/bin/thing-3.2
/bin/thing-3.2/include:/usr/include
/usr/include/SDL:/usr/local/include/SDL
/bin/thing/include/SDL/stan

Output Description

Expand it into its true form, for example:

/usr/local/include/SDL/stan

'''
import re

paths = '''/bin/thing:/bin/thing-3
/bin/thing-3:/bin/thing-3.2
/bin/thing-3.2/include:/usr/include
/usr/include/SDL:/usr/local/include/SDL
/bin/thing/include/SDL/stan'''

paths = paths.splitlines()

holding_list = []
for line in paths:
    first_slice = re.findall('\:(\/usr/local.*)', line)
    second_slice = re.findall('\/stan', line)
    if len(first_slice) >0:
        holding_list.append(first_slice[0])
    if len(second_slice) > 0:
        holding_list.append(second_slice[0])

output = holding_list[0] + holding_list[1]
print(output)