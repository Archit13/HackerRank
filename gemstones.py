# get number of rocks to compare
n = int(input())
rocks = set()
# for n number of input strings
for _ in range(n):
    # each rock is input separately
    rock = input()
    rocks.add(rock)

gems = set.intersection(rocks)
print(len(gems))