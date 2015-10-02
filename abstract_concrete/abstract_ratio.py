import sys
from collections import Counter

fid = sys.stdin
# function_words.txt
function_word_file = open(sys.argv[1], 'r').readlines()
# non-concrete-nouns-utf8.txt
abstract_word_file = open(sys.argv[2], 'r').readlines()

word_counter = Counter()
abstract_counter = Counter()
concrete_counter = Counter()
function_words = {}
abstract_words = {}

for line in function_word_file:
    line = line.strip()
    function_words[line] = {}

for line in abstract_word_file:
    line = line.strip()
    abstract_words[line] = {}

for line in fid:
    line = line.strip()
    line = line.lower()
    line = line.split()
    for word in line:
        word_counter[word] += 1

for word in word_counter:
    if word in abstract_words:
        abstract_counter[word] = word_counter[word]
    elif word in function_words:
        continue
    else:
        concrete_counter[word] = word_counter[word]


num_concrete = len(concrete_counter)
num_abstract = len(abstract_counter)

print abstract_counter

print "concrete:abstract", num_concrete, ":", num_abstract

