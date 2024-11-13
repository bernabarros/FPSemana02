word1 = set(input())
word2 = set(input())

letters = word1.intersection(word2)

sep = ""

answer = sep.join(sorted(letters))

print(answer)