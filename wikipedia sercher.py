import wikipedia

topic = input("What do you wan't to seacrh for: ")
lenght = input("how many paragraphs on that topic do you wan't: ")

#If the wikipedia page doesn't exist the code wil return an error
try:
    info = wikipedia.summary(topic,lenght)
    print(info)
except:
    print("couldn't find any info on that topic.")
