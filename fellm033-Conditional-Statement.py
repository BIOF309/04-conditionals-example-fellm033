pyg = 'ay'

original = input('Enter a word: ')

if len(original)>0 and original.isalpha():
    word = original.lower()
    first = word[0]
    word = original.lower()
    new_word = word[1:len(original)] + first + pyg
    print (new_word)

else:
    print ("Empty")
word = original.lower()
