latin = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')                                   #0-25 (26)
cyrillic = ('а','б','в','г','ґ','д','е','є','ж','з','и','і','ї','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ю','я')    #0-32 (33)
symbols = ('!','@','1','#','$','8','№','%','^','0','&','*','(',')','2','-','_','5','=','+','3',':',';','9','[',']','4','{','}','"',"'",'?','6',',','.','<','>','7',' ','`','~','—','|','’')

text = str(input("Input text to sipher:\n"))
print('Output:')

key = 1
changeKey = False

for char in text:
    # CAPSLOCK CHECK
    capslock = False
    if(char not in symbols):
        if(char == char.upper()):
            capslock = True
            char = char.lower()
    # LATIN ALPHABET
    if(char in latin):
        alphabet = latin
    # CYRILLIC ALPHABET
    elif(char in cyrillic):
        alphabet = cyrillic
    # OTHER SYMBOLS
    elif(char in symbols):
        alphabet = symbols
    # NOT A UKRAINIAN OR ENGLISH LANGUAGES
    else:
        print(f"\n// ERROR - Wrong language used > '{char}'.\n// Use only ukrainian or english languages!")
        break
    # MAIN CODE
    index = alphabet.index(char)
    size = len(alphabet)
    if(index+key >= 0 and index+key < size):
        result = (alphabet[index+key])
    elif(index+key >= size):
        cycle = 1
        while(index+key > size*cycle):
            cycle += 1
        result = (alphabet[(index+key)-(size*cycle)])
    else:
        cycle = -1
        while(index+key < size*cycle):
            cycle += -1
        result = (alphabet[(index+key)-(size*cycle)])
    # CHANGE KEY
    if(changeKey == True):
        if(key > 0):
             key += 2
        elif(key < 0):
             key -= 2
    # RESULT
    if(capslock == True):
        result = result.upper()
    else:
        result = result.lower()
    print(result, end='')
input()