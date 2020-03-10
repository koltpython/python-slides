
# Free Association Game

clues = ('rain', 'cake', 'glass', 'flower', 'napkin')

# Let's play a game. Give the user these words one by one and ask them to give you the first word that comes to their mind.
# Store these words together in a dictionary, where the keys are the clues and the values are the words that the user tells.
# We want another user to be able to learn the previous user's associations. For this reason, ask the user which word's association
# they want to learn and print the related word.
pairs = dict()

for word in clues:
    answer = input(f"What word comes to your mind when you see {word} ")
    pairs[word] = answer

print(pairs)

key = input("What do you want to learn? ")
while key != 'exit':
    print(pairs[key])
    key = input("What do you want to learn? ")

open("texts/my_text.txt", mode='w')