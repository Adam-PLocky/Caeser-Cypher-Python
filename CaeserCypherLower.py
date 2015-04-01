letters = list("abcdefghijklmnopqrstuvwxyz")#All the lower case letters of ASCII
translated = ""
while 1:#Inifinte loop
    enc_dec = input("Do you wish to Encrypt of Decrypt? Enter E or D: ").lower()
    if enc_dec == "e" or enc_dec == "d":#Checks they have entered an E or a D
        pos_neg = int((ord(enc_dec)-100.5)*2)#Turns "d" into a -1 and "e" into a +1 (needed to encrypt or decrypt)
        break#Leaves the loop
    else:
        print("Invalid Response. Please try again.")
string = input("Enter your message: ").lower()#Puts all messages in lower as that is all this program can do
while 1:#Inifinte loop
    indent = int(input("Enter a key number (1-26): "))#This is the key, this will be how much your text is offset by. Rember this, it is important!
    if indent < 1 or indent > 26:
        print("Invalid Option. Please try again.")
    else:
        break#Leaves loop
for i in range(len(string)):#Repeats for the length of your message
    string = list(string)#Turns your message into individual letters
    if string[i] == " ":
        translated += " "#If there is a space, it will leave it as a space
    else:
        num = ord(string[i])-97#Turns it into ascii, in relation to the charcters in var 'letters'.
        num += indent*pos_neg#Will either add(encrypt) or subtract(decrypt) the indent or key that you have chosen.
        num = num%26#num modulus 26(letters in the alphabet)
        translated += letters[num]#Adds the letter to this variable
    savedFile = open('Encrypted.txt', 'w')
    savedFile.write(translated)#Saves it to a file
    savedFile.close()
print("\nTranslation complete: " + translated)
