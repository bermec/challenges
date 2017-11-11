'''Checksums are a tool that allow you to verify the integrity of data (useful for networking,
security, error-correction, etc.). Though there are many different Checksum algorithms, the
general usage is that you give raw-data to your algorithm of choice, and a block of data
(usually smaller than the given data) is generated and can later be used by re-computing the
checksum and comparing the original and recent values.

A classic example for how helpful Checksums are is with data-networking: imagine you have a
packet of information that must be guaranteed the same after receiving it. Before sending the
data, you can compute its checksum, and send both blocks together. When received, the data can
be used to re-compute a checksum, and validate that the given checksum and your own checksum
are the same. The subject is much more complex, since there are issues of data-entropy and the
importance of the checksum's size compared to the raw data size.

This example is so common in network programming, one of the basic Internet networking
protocols (TCP) has it built-in!

Your goal will be more modest: you must implement a specific checksum algorithm (Fletcher's
16-bit Checksum) for given lines of text input. The C-like language pseudo-code found on
Wikipedia is a great starting point!

Note: Make sure to explicitly implement this algorithm, and not call into other code (libraries).
The challenge here is focused on your implementation of the algorithm.
Formal Inputs & Outputs
Input Description

On standard console input, you will first be given an integer N which ranges inclusively from
1 to 256. After this line, you will receive N-lines of ASCII text. This text will only contain
regular printable characters, and will all be on a single line of input.
Output Description

For each line of input, print the index (starting from 1) and the 16-bit Fletcher's checksum
as a 4-digit hexadecimal number.
Sample Inputs & Outputs
Sample Input

3
Fletcher
Sally sells seashells by the seashore.
Les chaussettes de l'archi-duchesse, sont-elles seches ou archi-seches ?

Sample Output

1 D330
2 D23E
3 404D

# No cheating, did not use hex(n) :)
'''

def dec_to_hex(n):
    hex_num = {10: 'A',
               11: 'B',
               12: 'C',
               13: 'D',
               14: 'E',
               15: 'F'}
    hex_list = []
    while True:
        num = n // 16
        if num > 9:
            numb = hex_num[num]
            hex_list.append(numb)
        else:
            hex_list.append(num)
        n = n - (num * 16)
        pass
        if n > 9:
            n = hex_num[n]
        hex_list.append(n)
        hex_string = ''
        for char in hex_list:
            hex_string += str(char)
        break
    return hex_string


if __name__ == '__main__':

    candidates = '''Fletcher
Sally sells seashells by the seashore.
Les chaussettes de l'archi-duchesse, sont-elles seches ou archi-seches ?'''

    candidates = candidates.splitlines()

    for message in candidates:
        sum1 = 0
        sum2 = 0

        for letter in range(0, len(message)):
            sum1 += ord(message[letter])
            sum2 += sum1

        checksum1 = sum1 % 255
        checksum2 = sum2 % 255
        hex_sum1 = dec_to_hex(int(checksum2))
        hex_sum2 = dec_to_hex(int(checksum1))
        print(hex_sum1 + hex_sum2)



