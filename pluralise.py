def pluralize(wordList):
    newWordList = []
    wordCount = 0
    for word in wordList:
        for wordInst in wordList:
            if wordInst == word:
                wordCount += 1
        if wordCount >= 2:
            newWordList.append(word + "s")
        else:
            newWordList.append(word)

    return newWordList
