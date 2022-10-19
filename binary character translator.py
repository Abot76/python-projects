import string
alphabet = list(string.ascii_lowercase)
character1 = str(input("enter a word or a sentance: "))
StringLenght = len(character1)
CurrentLetterIndex = 0
CurrentLetter = character1[CurrentLetterIndex]
EncodedString = ""



def convert(letter):
    if letter == " ":
        output = "00100000"

    else:
        letter2 = letter
        letter = letter.lower()
        Value = alphabet.index(letter)
        Value += 1

        #Spremeni vrednost v binarno število
        Value = bin(Value)
        str(Value)
        Value = Value[2:]

        #Zrčuna koliko ničelj mora dodat na začetku da bo string dolg 5 mest
        lenght = len(Value)
        int(lenght)
        required = 5 - lenght

        #Doda potrebne ničle na začetek stringa
        i = 0
        Value1 = 0
        while i < required:
            Value1 = str(Value1) + str(Value)
            Value = Value1
            Value1 = 0
            i += 1

        
        if letter2 == letter: 
            output = "011"+Value

        else:
            output = "010"+Value

    return output


for q in range(StringLenght):
    
    EncodedString = str(EncodedString) + str(convert(CurrentLetter)) #Doda novo črko v EncoderString

    CurrentLetterIndex += 1  #Premakne kazalec na naslednjo črko

    if CurrentLetterIndex < StringLenght: #preveri če kazalec kaže na nemogočo pozicijo in če je ne poskusi shraniti naslednje črke v CurrentLetter
        CurrentLetter = character1[CurrentLetterIndex]


print(EncodedString)
