from Bio import SeqIO
from Bio import Seq
import sys
from kmp import preprocessNeedle, KMPSearch

seq = next(SeqIO.parse(sys.argv[1], "fasta")).seq

# Check answer

def find_all(a_string, sub):
    result = []
    k = 0
    while k < len(a_string):
        k = a_string.find(sub, k)
        if k == -1:
            return result
        else:
            result.append(k)
            k += 1
    return result

print(find_all(str(seq[:100]), "TT"))
KMPSearch('TT', str(seq[:100]))
