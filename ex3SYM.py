# shiftcipher
word = "HGHUUT"
word2 = "MBQ"

startingASCII = 65
endingASCII = 91

for i in range(65, 91):
    print(str(i) + "\n")
    newWord = ""
    for a in word2:
        new_char = (((ord(a)+i) - startingASCII) % 26) + startingASCII
        newWord += chr(new_char)
    print(newWord + "\n")

