'''
If you've ever seen Breaking Bad, you might have noticed how some names
in the opening credit sequence get highlights according to symbols of
elements in the periodic table. Given a string as input, output every
possible such modification with the element symbol enclosed in brackets
and capitalized. The elements can appear anywhere in the string, but you
must only highlight one element per line, like this:

$ ./highlight dailyprogrammer
dailypr[O]grammer
daily[P]rogrammer
dail[Y]programmer
da[I]lyprogrammer
dailyprog[Ra]mmer
daily[Pr]ogrammer
dailyprogramm[Er]
dailyprogr[Am]mer


'''
import re

symbols = ["Ac","Ag","Al","Am","Ar","As","At","Au","B","Ba","Be","Bh","Bi",
"Bk","Br","C","Ca","Cd","Ce","Cf","Cl","Cm","Cn","Co","Cr","Cs",
"Cu","Db","Ds","Dy","Er","Es","Eu","F","Fe","Fl","Fm","Fr","Ga",
"Gd","Ge","H","He","Hf","Hg","Ho","Hs","I","In","Ir","K","Kr","La",
"Li","Lr","Lu","Lv","Md","Mg","Mn","Mo","Mt","N","Na","Nb","Nd","Ne",
"Ni","No","Np","O","Os","P","Pa","Pb","Pd","Pm","Po","Pr","Pt","Pu",
"Ra","Rb","Re","Rf","Rg","Rh","Rn","Ru","S","Sb","Sc","Se","Sg","Si","Sm",
"Sn","Sr","Ta","Tb","Tc","Te","Th","Ti","Tl","Tm","U","Uuo","Uup","Uus","Uut",
"V","W","Xe","Y","Yb","Zn","Zr"]

#print(symbols)


txt = '''   I. A Scandal in Bohemia
  II. The Red-headed League
 III. A Case of Identity
  IV. The Boscombe Valley Mystery
   V. The Five Orange Pips
  VI. The Man with the Twisted Lip
 VII. The Adventure of the Blue Carbuncle
VIII. The Adventure of the Speckled Band
  IX. The Adventure of the Engineer's Thumb
   X. The Adventure of the Noble Bachelor
  XI. The Adventure of the Beryl Coronet
 XII. The Adventure of the Copper Beeches'''

# each line is now a list
txt = txt.split('\n')
segment = ''
symbol_list = ['Th']
for x in range(0, len(txt)):
    # first list
    line = txt[x]
    for y in range(0, len(line)):
        segment = line[y:y + 2]
        try:
            s = segment.capitalize()
        except:
            continue

        segment_replacement = '(' + s + ')'

        # symbol_list to check for duplicates
        if s in symbols and s not in symbol_list:
            line2 = re.sub(segment, segment_replacement, line)
            print(line2)
            symbol_list.append(s)
            line2 = ''
            break

