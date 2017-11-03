pcent = input('Percent?  "q" to quit ')

denom = 674
while pcent != 'q':
    if pcent == 'q':
        exit()
    else:
        output = int((int(pcent) / denom) * 100) + 10
        print('{0}{1}{2)'.format(pcent, ' percent = ', output))