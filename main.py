phrase = []
sym = input("What symbol do you want to remove? ")
words = input("Please input the phrase: ")
cleanedList = words.split(sym)
'''
phrase.append(words)
while phrase[-1] != "-":
	words = input("Please input the phrase: ")
	phrase.append(words)
for part in phrase:
'''
cleanWords = " ".join(cleanedList)
print("\n",cleanWords)
