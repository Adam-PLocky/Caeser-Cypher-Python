letters = list("""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""")#All the printable characters in ASCII
translated = ""
while 1:#Infinite loop
    enc_dec = input("\nDo you want to Encrypt or Decrypt your text? \n(Just enter an E or  a D) ").lower()
    if enc_dec == "e" or enc_dec == "d":#Checks they have entered an E or a D
        pos_neg = int((ord(enc_dec)-100.5)*2)#Turns "d" into a -1 and "e" into a +1 (needed to encrypt or decrypt)
        break#Leaves the loop
    else:
        print("You gave an aswer which I cannot comprehend. \n(I am only a computer after all!)\nPlease try again.")
string = input("\nPlease enter your message here: ")
while 1:#Inifinte loop
    indent = round(float(input("\nEnter your cypher number between 1-26: ")))#Float-number with deciamls, round turns it into nearest integer.
    if indent < 1 or indent > 26:#Checks they enrtered a number between 1 and 26
        print("That's not between 1 and 26 silly! \nPlease try again.")
    else:
        break#Leaves loop
birth = round(float(input("Please enter your birth year-\nIt is important!")))#Float-number with deciamls, round turns it into nearest integer.
while 1:#Infinite loop
    if birth < 1900 or birth > 2015:
        birth = round(float(input("Franklly that would be impossible \nPlease enter your real DoB.")))
    else:
        break#Leaves loop
for i in range(len(string)):#Repeats for the length of your message
    string = list(string)#Turns your message into individual letters
    if string[i] == " ":
        translated += " "#If there is a space, it will leave it as a space
    else:
        num = ord(string[i])-33#Turns it into ascii, in relation to the charcters in var 'letters'.
        num += (indent+(((i+1)**birth)%17)+i)*pos_neg#Complicated maths to make it more secure!(you can really put anything here)-there is a basic version of this in the simple version/
        num = num%94#num modulus 94(number of characters used)
        translated += letters[num]#Adds the letter to this variable
    savedFile = open('Encrypted.txt', 'w')
    savedFile.write(translated)#Saves it to a file
    savedFile.close()
print("\nTranslation complete: " + translated)
