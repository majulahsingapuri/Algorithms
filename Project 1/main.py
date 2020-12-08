from Bio import SeqIO
from Bio import Seq
import sys
from kmp.kmp import KMPhn
from brute_force.brute_force import bruteForce

needle = sys.argv[1]
seq = next(SeqIO.parse(sys.argv[2], "fasta")).seq

print(f'KMP found: {KMPhn(needle, seq)}')
print(f'Brute Force found: {bruteForce(needle, seq)}')
