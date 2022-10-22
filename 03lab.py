top = 5 # top > 0!
opt = str(input(f"A - TOP {top} REPEATING WORDS (>3 char)\nB - ALPHABET SORT\nC - TOP {top} WIDE WORDS (>3 char)\nChoose option - A/B/C: ")).upper()
text = str(input("Input text:\n"))
text = text.split(" ")
t, tname = [], []
for i in range(top):
    t.append(0)
    tname.append('')
for word in text:
    index = text.index(word)
    text[index] = word.lower()
    while(word == '' or word == ' ' or word[0].isalnum() == False or word[-1].isalnum() == False):
        if(word == '' or word == ' '):
            text.pop(index)
            break
        elif(word[0].isalnum() == False):
            word = word[1:].lower()
            text[index] = word
        elif(word[-1].isalnum() == False):
            word = word[:-1].lower()
            text[index] = word
# OPT A AND C HAVE SAME CODE
def top5(filter):
    for word in text:
        if(word in tname or len(word) <= 3 ):
            continue
        count = filter(word)
        find = False
        place = 0
        while(find == False):
            if(count > t[place]):
                if(t[place] > 0):
                    cycle = top-place-1
                    nplace = -1
                    while(cycle > 0):
                        t[nplace] = t[nplace-1]
                        tname[nplace] = tname[nplace-1]
                        nplace -= 1
                        cycle -= 1
                t[place] = count
                tname[place] = word
                find = True
            elif(place < top-1):
                place += 1
            else:
                find = True
    place = 0
    while(place < top and t[place] > 0):
        print(f"Top{place+1} = {tname[place]}[{t[place]}]")
        place += 1
# TOP REPEATING WORDS
if(opt == "A"):
    top5(text.count)
# ALPHABET WORD SORT, NO REPEATING
elif(opt == "B"):
    text2 = []
    for word in text:
        if(word in text2 or word[0].isnumeric() == True or len(word) <= 3):
            continue
        text2.append(word)
    text2.sort()
    for word in text2:
        print(word)
# TOP WIDE WORDS
elif(opt == "C"):
    top5(len)
else:
    print(f"ERROR - Wrong option > '{opt}'")
input()