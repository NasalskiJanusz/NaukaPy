# Write a function that takes in a string of one or more words,
# and returns the same string,
# but with all words that have five or more letters reversed
# (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
#
# Examples:
#
# "Hey fellow warriors"  --> "Hey wollef sroirraw"
# "This is a test        --> "This is a test"
# "This is another test" --> "This is rehtona test"

# 2nd try
'''def spin_words(sentence):
    lenght = len(sentence)
    sen = sentence.split()
    temp = ""
    for i in sen:
        if i == ' ':
            lenght -= 1
        if len(i) >= 5:
            print(i)
            temp = i[::-1]


    print(temp)
'''





# 1st try
# spin_words("abcde")
# 2nd try
# spin_words("Second try")

# wynik = ""
# for i in st:
#     if len(i) >=5:
#         i = i[::-1]
#         wynik += i
#     else:
#         wynik += i

# end code
def spin_words(sentence):
    # splitted sentecne list
    stSplit = sentence.split()
    # result variable
    result = ""
    # iterating using index
    for i in range(len(stSplit)):
        # check lenght of word
        if len(stSplit[i]) >= 5: result += (stSplit[i][::-1]) # reversing
        else: result += (stSplit[i])
        if i != len(stSplit) - 1: result += (" ")

    return result








# input
st = "I will make some sandwitches for you guys"
# split
stSplit = st.split()
# result
result = ""
# i = index
for i in range(len(stSplit)):
    if len(stSplit[i]) >= 5:
        result += (stSplit[i][::-1])
    else:
        result += (stSplit[i])
    if i != len(stSplit)-1:
        result += (" ")
print(result)

# print("\nNew: ",newList)
# print("\nResult: ",result)
#print("\n[-1]stSplit: ",stSplit[-1])
# print("\nSplit list: ",splitList)