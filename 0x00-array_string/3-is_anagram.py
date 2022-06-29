#!/usr/bin/python3

def isAnagram(str1, str2):
    dictLetters = {}
    for i in range(len(str1)):
        if str1[i] not in dictLetters:
            dictLetters[str1[i]] = 1
        else:
            dictLetters[str1[i]] += 1
    for j in range(len(str2)):
        if str2[j] not in dictLetters or dictLetters[str2[j]] == 0:
            return  False
        else:
            dictLetters[str2[j]] -= 1
    for value in dictLetters.values():
        if value > 0:
            return False
    return True