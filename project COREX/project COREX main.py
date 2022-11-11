import pyttsx3 # for speech services
import os # for file managment and storing long term data
import math
import wikipedia # for information
import datetime # mainly for timestamps
#import maskpass # for passwords
import time # for wait functions
import colorama # for ancy text
import random
import string # for encryption

sound_config = open("config/sound.txt")
sound = sound_config.read()
engine = pyttsx3.init()
alphabet = list(string.ascii_letters)
specialCharacters = ["1",".",",",":",";","!","#","%",'""',"(",")","/","?","+","-","*","_","2","3","4","5","6","7","8","9","0","°","&","=","š","č","ž","Š","Č","Ž"]

memory1 = 0
memory2 = 0
memory3 = 0
memory4 = 0
memory5 = 0
memory6 = 0
memory7 = 0
memory8 = 0
memory9 = 0
memory10 = 0

#function for talking
def talk(text):
    engine.say(text)
    engine.runAndWait()

#function for saving to VM memory
def saveToMemory(adress,value):
    global memory1
    global memory2
    global memory3
    global memory4
    global memory5
    global memory6
    global memory7
    global memory8
    global memory9
    global memory10
    if adress == "1":
        memory1 = value
    elif adress == "2":
        memory2 = value
    elif adress == "3":
        memory3 = value
    elif adress == "4":
        memory4 = value
    elif adress == "5":
        memory5 = value
    elif adress == "6":
        memory6 = value
    elif adress == "7":
        memory7 = value
    elif adress == "8":
        memory8 = value
    elif adress == "9":
        memory9 = value
    elif adress == "10":
        memory10 = value
    else:
        print("An error occured. error code: 0x00")

def calculate(equasion):
          
    result = eval(equasion)
    return result

def internetSearch(query):
    try:
        output = wikipedia.summary(query, 10)
    except:
        output = "Could not find anything. Sorry"
    return output

def systemCommand(command):
    os.system(command)


#functions for encryption and decryption
def encode(letter4):
    global encrypt

    Value = int(letter4)
    Value += 17

                    
    encrypt = Value
    encrypt = int(encrypt) - 16
    #Spremeni vrednost v binarno število
    Value = bin(Value)
    str(Value)
    Value = Value[2:]

    #Zrčuna koliko ničelj mora dodat na začetku da bo string dolg 5 mest
    lenght = len(Value)
    int(lenght)
    required = 6 - lenght

    #Doda potrebne ničle na začetek stringa
    i = 0
    Value1 = 0
    while i < required:
        Value1 = str(Value1) + str(Value)
        Value = Value1
        Value1 = 0
        i += 1

    output = "11"+Value
    return output


def convert(letter):
    if letter == " ":
        output = "10000000"

    else:
        letter2 = letter


        if letter in specialCharacters:
            Value = specialCharacters.index(letter)
            letter2 = "char"

        else:
                    
            letter = letter.lower()
            Value = alphabet.index(letter)
        Value += 1
        Value = Value + encrypt
                    

        #Spremeni vrednost v binarno število
        Value = bin(Value)
        str(Value)
        Value = Value[2:]

        #Zrčuna koliko ničelj mora dodat na začetku da bo string dolg 5 mest
        lenght = len(Value)
        int(lenght)
        required = 6 - lenght

        #Doda potrebne ničle na začetek stringa
        i = 0
        Value1 = 0
        while i < required:
            Value1 = str(Value1) + str(Value)
            Value = Value1
            Value1 = 0
            i += 1

                    
        if letter2 == letter: 
            output = "01"+Value

        elif letter2 == "char":
            output = "10"+Value

        else:
            output = "00"+Value

    return output

#Dekodira kluč za šifriranje
def decode(letter5):       
    letter5 = letter5[2:]
                    
    letter5 = int(letter5, 2)
    letter5 = int(letter5) - 16
    return str(letter5)


#Dekodira sporočilo z ključem
def convert2(letter,key):
    if letter[0] == "1":
                
        letter = letter[2:]
        letter = int(letter, 2)

        if letter == 0:
            letter = str(" ")

        else:
            letter = int(letter) - 1
            letter = int(letter) - int(key)
            letter = specialCharacters[int(letter)]
            str(letter)

    else:
        letter = letter[1:]
        #Ugotovi če je črka upper ali lower case
        if letter[0] == "0":
            case = 0
                        
        else:
            case = 1

        #Spremeni binarno število v decimalno
        letter = letter[1:]
        letter = int(letter, 2)

        if letter == 0:
            letter = " "

        else:
            if case == 0:
                            
                letter = int(letter+26)

            letter = int(letter) - 1
            letter = int(letter) - int(key)

            letter = alphabet[int(letter)]
            str(letter)

    return str(letter)

def autoEncrypt(message_data):
    encrypt = ""
    encryption = ""
    encryption_key = ""

    character1 = str(message_data)
    StringLenght = len(character1)
    CurrentLetterIndex = 0
    CurrentLetter = character1[CurrentLetterIndex]
    EncodedString = ""

    encryption_key = random.randint(6,25)

    encryption = str(encode(encryption_key))

    for q in range(StringLenght):
                    
        EncodedString = str(EncodedString) + str(convert(CurrentLetter)) #Doda novo črko v EncoderString

        CurrentLetterIndex += 1  #Premakne kazalec na naslednjo črko

        if CurrentLetterIndex < StringLenght: #preveri če kazalec kaže na nemogočo pozicijo in če je ne poskusi shraniti naslednje črke v CurrentLetter
            CurrentLetter = character1[CurrentLetterIndex]

    encryption = str(encryption) + str(EncodedString)
    return encryption

def autoDecrypt(message_data):
    encrypt = ""
    encryption = ""
    encryption_key = ""

    character1 = str(message_data)
    StringLenght = (len(character1) // 8) - 1
    letter3 = ""
    EncodedString = ""

    i = 0
    while i < 8:
        encryption_key = str(encryption_key) + str(character1[i])
        i += 1

    character1 = str(character1[8:])
    key1 = decode(encryption_key)

    for q in range(StringLenght):
        letter3 = ""

        i = 0
        while i < 8:
            letter3 = str(letter3) + character1[i]
            i += 1

        character1 = character1[8:]
        EncodedString = EncodedString + convert2(letter3,key1)
    return EncodedString







list = os.listdir("user")
if "username.txt" in list: #checks if a user account already exists
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()
    l_p = autoDecrypt(l_p)
    l_n = autoDecrypt(l_n)
    
    

    l_p_tmp = input("Enter the password: ")


    if  l_p_tmp == l_p:
        l_s = "in_"
        with open("user/status.txt","w") as fp:
            fp.write(l_s)
            fp.close()
            pass
        print("Logged in.")
        if sound == "1":
            talk("Welcome "+l_n)
    else:
        print("Incorrect password.")
        quit()
        
else:
    print("No users present.")
    name = autoEncrypt(input("Enter a username: "))
    pas = autoEncrypt(input("Enter a password: "))

    with open('user/username.txt', 'w') as f:
        f.writelines(name)
    with open('user/password.txt', 'w') as f:
        f.writelines(pas)

    quit()
    

while True:

    comm = input("Enter a command: ")
    if "sound" in comm:
        sound = comm[7:]
        if sound == "n":
            sound = "1"
            talk("sound is on")
        else:
            sound = "0"
        
    elif "calc" in comm:
        if "calculate" in comm:
            comm = comm[10:]
        else:
            comm = comm[5:]
        try:
            result = calculate(comm)
            print(result)

            if sound == "1":
                talk("that's "+ str(result)+".")
        except:
            print("Sorry, couldn't calculate that.")
            talk("Sorry, couldn't calculate that.")

    elif "log" in comm:
        l_s = autoEncrypt("out")

        with open("user/status.txt","w") as fp:
            fp.write(l_s)
            fp.close()
            pass
        print("You are now logged out. Goodbye.")
        if sound == "1":
            talk("You are now logged out. Goodbye.")
        quit()

    elif "google" in comm:
        query = comm[7:]
        query = internetSearch(query)
        print(query)
        if sound == "1":
            talk(query)

    elif "cmd" in comm:
        while True:
            command = input(">_ ")
            if command == "exit":
                break
            os.system(command)
    
    elif "quit" in comm:
        print("Goodbye.")
        if sound == "1":
            talk("goodbye.")

        quit()

    else:
        print('"'+comm+'" not recognized as an internal or an external command.')
        if sound == "1":
            talk('"'+comm+'" not recognized as an internal or an external command.')

