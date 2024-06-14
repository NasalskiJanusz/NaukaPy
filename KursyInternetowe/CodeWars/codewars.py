def ciecie(s):
    nowa_lista=[]
    for i in range(0, len(s), 2):            
        fragment = s[i:i + 2]
        if len(fragment) < 2:
            fragment += "_"
        nowa_lista.append(fragment)

    return nowa_lista

s=input("Enter a string: ")
print(ciecie(s))

