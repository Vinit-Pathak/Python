anime = 'Naruto'
Len = len(anime)
print(Len)
print(anime[0:6])  #including 0 but not 6
print(anime[1:6])  #including 1 but not 6
print(anime[:5])
print(anime[:])
print(anime[0:-3])   #print(anime[0:len(anime)-3]) by default
print(anime[-3:-1])   

nm = "Harry"
print(nm[-4:-2])

alphabets = "ABCDEF"
for i in alphabets:
    print(i)