phrase = input()
char_count = 0
answer = {}

phrase = phrase.split()

for word in phrase:
    char_count = len(word)
    answer[word] = char_count

print(answer)