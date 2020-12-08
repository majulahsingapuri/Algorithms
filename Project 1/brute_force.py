from Bio import SeqIO
from Bio import Seq
import time

haystack = next(SeqIO.parse("/Users/bhargav/Downloads/GCF_000264905.1_Stehi1_genomic.fna", "fasta")).seq
needle = "AAAAATTA"

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

check = time.perf_counter()
print(find_all(str(haystack), needle))
check = time.perf_counter() - check

print(f"\n\nCheck took {check:0.4f} seconds\n\n")

needleLength = len(needle)
haystackLength = len(haystack)


def bruteForce(needle, haystack):

    found = False
    for haystackIdx in range(0, haystackLength - needleLength + 1):

        needleIdx = 0
        # loop through needle characters
        while (needleIdx < needleLength):
            # mismatch: return needle index to 0, compare with next char in haystack
            if haystack[needleIdx + haystackIdx] != needle[needleIdx]:
                break
            else:  # compare next char in needle
                needleIdx += 1

        if needleIdx == needleLength:
            found  = True
            print(haystackIdx, end = ", ")

    if found is False:
        print("Pattern not found")
    print()

brute = time.perf_counter()
bruteForce(needle, haystack)
brute = time.perf_counter() - brute
print(f"\n\nBrute took {brute:0.4f} seconds")
