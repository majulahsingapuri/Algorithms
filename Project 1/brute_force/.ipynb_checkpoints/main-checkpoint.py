from brute_force import bruteForce

from datetime import datetime, date
from Bio import SeqIO
from Bio import Seq
import sys

needle = sys.argv[1]
haystack = next(SeqIO.parse(sys.argv[2], "fasta")).seq

start = datetime.now()
bruteForce(needle, haystack)
end = datetime.now()
duration = end - start
print(duration.total_seconds())
