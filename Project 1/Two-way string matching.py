from Bio import SeqIO
from Bio import Seq
import time

haystack = next(SeqIO.parse("/Users/bhargav/Downloads/GCF_000264905.1_Stehi1_genomic.fna", "fasta")).seq
needle = "GGTGGT"

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

def maxSuf(needle, needleSize):
    maxSuffix = -1
    lastRest = 0
    k = p = 1

    while (lastRest + k < needleSize):
        a = needle[lastRest + k]
        b = needle[maxSuffix + k]

        if (a < b):
            lastRest += k
            k = 1
            p = lastRest - maxSuffix
        elif (a == b):
            if (k != p):
                k += 1
            else:
                lastRest += p
                k = 1
        else:
            maxSuffix = lastRest
            lastRest = maxSuffix + 1
            k = p = 1

    return (maxSuffix, p)

def maxSufTilde(needle, needleSize):
    maxSuffix = -1
    lastRest = 0
    k = p = 1

    while (lastRest + k < needleSize):
        a = needle[lastRest + k]
        b = needle[maxSuffix + k]

        if (a > b):
            lastRest += k
            k = 1
            p = lastRest - maxSuffix
        elif (a == b):
            if (k != p):
                k += 1
            else:
                lastRest += p
                k = 1
        else:
            maxSuffix = lastRest
            lastRest = maxSuffix + 1
            k = p = 1

    return (maxSuffix, p)

def memcmp(stringA, stringB, byte):
    for i in range(byte):
        if (stringA[i] != stringB[i]):
            return False

    return True

def TwoWayStringMatch(needle, haystack):
    needleSize = len(needle)
    haystackSize = len(haystack)
    rightCounter, p = maxSuf(needle, needleSize)
    leftCounter, q = maxSufTilde(needle, needleSize)

    if (rightCounter > leftCounter):
        critPosition = rightCounter
        period = p
    else:
        critPosition = leftCounter
        period = q

    if (memcmp(needle, needle[period:], critPosition + 1)):
        leftCounter = 0
        memory = -1

        while (leftCounter <= haystackSize - needleSize):
            rightCounter = (critPosition if critPosition > memory else memory) + 1
            while (rightCounter < needleSize and needle[rightCounter] == haystack[rightCounter + leftCounter]):
                rightCounter += 1
            
            if (rightCounter >= needleSize):
                rightCounter = critPosition

                while (rightCounter > memory and needle[rightCounter] == haystack[rightCounter + leftCounter]):
                    rightCounter -= 1
                if (rightCounter <= memory):
                    print(leftCounter, end = ", ")
                
                leftCounter += period
                memory = needleSize - period - 1
            else:
                leftCounter += (rightCounter - critPosition)
                memory = -1
    else:
        period = ((critPosition + 1) if (critPosition + 1) > (needleSize - critPosition - 1) else (needleSize - critPosition - 1)) + 1
        leftCounter = 0

        while (leftCounter <= haystackSize - needleSize):
            rightCounter = critPosition + 1
            while (rightCounter < needleSize and needle[rightCounter] == haystack[rightCounter + leftCounter]):
                rightCounter += 1
            
            if (rightCounter >= needleSize):
                rightCounter = critPosition

                while (rightCounter >= 0 and needle[rightCounter] == haystack[rightCounter + leftCounter]):
                    rightCounter -= 1
                if (rightCounter < 0):
                    print(leftCounter, end = ", ")
                
                leftCounter += period
            else:
                leftCounter += (rightCounter - critPosition)

if __name__ == "__main__":
    
    twoway = time.perf_counter()
    TwoWayStringMatch(needle, haystack)
    twoway = time.perf_counter() - twoway
    print(f"\n\nTwoWay took {twoway:0.4f} seconds")

    check = time.perf_counter()
    print(find_all(str(haystack), needle))
    check = time.perf_counter() - check
    print(f"\n\nCheck took {check:0.4f} seconds")