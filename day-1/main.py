import sys
from collections import Counter
# sys.stdout = open('./input.txt', 'w')
file = open('./day-1/input.txt', 'r')
locations = file.readlines()

# for index, line in enumerate(locations):
#     print("Line {}: {}".format(index, line.strip()))

sum = 0
list_a = []
list_b = []

for location in locations:
    a, b = map(int, location.split())
    list_a.append(a)
    list_b.append(b)

list_a.sort()
list_b.sort()

## Part 1
for i in range(len(list_a)):
    sum += abs(list_a[i] - list_b[i])

print(sum)

## Part 2
number_occurrences_b = Counter(list_b)

similarity_score = 0

for i in range(len(list_a)):
    similarity_score += list_a[i] * number_occurrences_b[list_a[i]]

print(similarity_score)