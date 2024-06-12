fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits.add("orange")                            #add to set

                                                #update (add set to set)
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
fruits.remove("banana")                         #remove banana
fruits.discard("banana")                        #discard banana
print(fruits)


# --------------------------------------SET------------------------------------------
            #collection which is unordered, unindexed. No duplicate values
            #Set items are unchangeable, but you can remove items and add new items.

            #set jest o wiele szybszy od listy z uwagi na to, że nie jest posegregowany
            #np. mając set z trzema danymi, po kilkukrotnym wywołanu setu zauważymi, że
            #set wywołuje nasze dane w losowej kolejnośći
            #JEŻELI BĘDĄ ZDUPLIKOWANE DANE TO WYŚWIETLI JĄ TYLKO RAZ NIE PATRZĄC NA TO ILE ICH TAM JEST

rzeczy_kuchenne = {'nóż', 'widelec', 'łyżka'}
naczynia = {'talerz płaski', 'talerz głęboki', 'kubek', 'nóż'}

rzeczy_kuchenne.update(naczynia)               #dodaje "naczynia" do "rzeczy_kuchenne"
obiad = rzeczy_kuchenne.union(naczynia)         #nowa zmienna która łączy te dwa sety
print(rzeczy_kuchenne.difference(naczynia))     #wypisuje tylko dane które się różnią między setami
print(rzeczy_kuchenne.intersection(naczynia))   #wypisuje dane które są takie same w obu setach

rzeczy_kuchenne.add("wazówka")
rzeczy_kuchenne.remove("widelec")


for i in obiad:
    print(i, end=", ")

