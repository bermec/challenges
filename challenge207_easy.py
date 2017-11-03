'''
For this week my theme is bioinformatics, I hope you enjoy the taste of the field
through these challenges.
Description

DNA - deoxyribonucleic acid - is the building block of every organism.
It contains information about hair color, skin tone, allergies, and more.
It's usually visualized as a long double helix of base pairs. DNA is composed
of four bases - adenine, thymine, cytosine, guanine - paired as follows: A-T and G-C.

Meaning: on one side of the strand there may be a series of bases

A T A A G C

And on the other strand there will have to be

T A T T C G

It is your job to generate one side of the DNA strand and output
the two DNA strands. Your program should take a DNA sequence as
input and return the complementary strand.
Input

A A T G C C T A T G G C

Output

A A T G C C T A T G G C
T T A C G G A T A C C G

Extra Challenge

Three base pairs make a codon. These all have different names based on what
combination of the base pairs you have. A handy table can be found here.
The string of codons starts with an ATG (Met) codon ends when a STOP codon is hit.

For this part of the challenge, you should implement functionality for translating
the DNA to a protein sequence based on the codons, recalling that every generated
DNA strand starts with a Met codon and ends with a STOP codon. Your program should
take a DNA sequence and emit the translated protein sequence, complete with a
STOP at the terminus.
Input

A T G T T T C G A G G C T A A

Output

A T G T T T C G A G G C T A A
Met Phe Arg Gly STOP

'''

dna = 'A A T G C C T A T G G C'
dna_split = dna.split()
comp_strand = ''

for letter in dna_split:
    if letter == 'A':
        letter = 'T'
    elif letter == 'T':
        letter ='A'
    elif letter == 'C':
        letter = 'G'
    else:
        letter = 'C'
    comp_strand += letter + ' '
print(dna)
print(comp_strand)

