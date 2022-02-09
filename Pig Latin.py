# Vowels and consonants, accounting for capital letters
vowels = "aeiouyYAEIOU"
consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

while True:
    # Variable for user input
    userInput = input("Enter a word or phrase to be translated into pig latin : ")

    if userInput == 0:
        break
    else:
        pass

    # Variables for storing words in sentences
    splitInput = userInput.split(" ")
    wordList = []
    sentenceList = []

    # Splitting words from sentence into lists with their letters
    for i in splitInput:
        wordList.append(list(i))

    # Translating based on the first letter of each word
    for word in wordList:
        if word[0] in vowels:
            word = "".join(word)
            word += "yay"
        elif word[0] in consonants:
            firstLetter = word.pop(0)
            word = "".join(word)
            word += firstLetter + "ay"
        else:
            pass
        sentenceList.append(word)

    # Making final sentence and capitalizing first word
    sentenceList[0] = sentenceList[0].capitalize()
    finalSentence = " ".join(sentenceList)
    print("\n" + finalSentence + "." + "\n")
