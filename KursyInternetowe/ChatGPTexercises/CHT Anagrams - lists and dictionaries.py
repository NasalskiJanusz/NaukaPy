# write code to sort anagrams with function that
# returns dictionary of them

# function to group anagrams
def group_anagrams(listOfWords):
    # dictionary to save anagrams
    anagrams = {}

    for word in listOfWords:
        # soring letters in word so we can make key
        # we need key to compare it with other words key's
        key = ''.join(sorted(word))

        # adding key if it's not yet in dictionary
        if key not in anagrams:
            anagrams[key] = []

        # add word to correct list if we found 2 == keys
        anagrams[key].append(word)

    # return dictionary as list
    return list(anagrams.values())



test1 = ["rat", "tar", "art", "car", "arc"]
print("Test1 samples: ",test1)
print("Result 1:",group_anagrams(test1))
# Result: [['rat', 'tar', 'art'], ['car', 'arc']]

test2 = ["apple", "pale", "leap", "plea", "lap", "pal"]
print("\n\nTest2 samples: ",test2)
print("Result 2:",group_anagrams(test2))
# Result: [['apple'], ['pale', 'leap', 'plea'], ['lap', 'pal']]





















