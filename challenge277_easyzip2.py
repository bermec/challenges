import re

holding_list = []

with open('277_test.txt') as f:
    for line in f:
        line = line.strip('\n')
        #print(line)
        extract = re.findall('[\s\S]', line)
        #print(extract)
        holding_list.append(extract)



#Your list of lists.
#uberlist = ( list1, list2, list3 )

#No sense in duplicating this definition multiple times.
#Define it up front.
uberRange = range( len(holding_list) );

#Since each will be the same length, you can use one range.
for i in range( len(holding_list) ):
    # Iterate through the sub lists.
    for j in holding_list:
        #Output
        print(holding_list[ j ][ i ])