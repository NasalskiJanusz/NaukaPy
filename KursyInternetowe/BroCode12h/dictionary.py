# --------------------------------------DICTIONARY------------------------------------------
                    #Nie uporządkowany zbiór danych    key:value jak w bazach danych
                    #Szybkie wyjmowanie danych
                    #Można dodać/usunąć klucz i wartość w każdym momencie

capitals = {'USA':'Washington',
            'Russia':'Moscow',
            'India':'Delhi',
            'Japan':'Tokyo'}

capitals["Poland"] = "Warsaw"

print(capitals['Japan'])              #wywołanie klucza powoduje wypisanie wartości
print(capitals.get('Germany'))        #sprawdzenie czy Germany jest kluczem, jeśli nie python odda "None"
print(capitals.keys())                #wydrukuje same klucze
print(capitals.values())              #wydrukuje same wartości
print(capitals.items())               #print (key, value), print whole dictionary
capitals.update({'Germany':'Berlin'})
capitals.pop('India')                   #usuwanie po kluczu
capitals.clear()                        #wyzeruje
for key,value in capitals.items():      #drukowanie wszystkiego za pomocą pętli for
    print(key,value)