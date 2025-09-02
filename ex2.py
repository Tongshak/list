word = "dod"
dictionary={}

for character in word:
        if character in dictionary:
                dictionary[character]+=1
        else:

                dictionary[character] = 1
for key in dictionary:
        if dictionary[key]==1:
                print(key)
