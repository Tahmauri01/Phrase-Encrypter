from random import choice as choice

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']        #List of characters

line = input("Type what you want to encrypt: ")
type = input("What type of encryption do you want: ")
if 'caesar' in type:
    numba = int(input("Type how many letters do you want to encrypt it by: "))
key = input("What do you want your key to be: ")

class Encrypter:      #Ways to encrypt

    def __init__(self, phrase, num, pswd):    #Initializes the phrase and the copy of the phrase that will be created
        self.phrase = phrase  
        self.num = num      
        self.letter = 0
        self.pswd = pswd
    
    def caesar(self):      #Makes a Caeser Cipher
        phrase_list = list(self.phrase)           #Makes phrase into a list
        for char in phrase_list:
            
            if phrase_list[self.letter].isalpha() == False:         #If the character is a space, it will ignore it
                phrase_list[self.letter] = phrase_list[self.letter]

            if phrase_list[self.letter].isupper() == True:            #Checks if character is uppercase
                phrase_list[self.letter] = phrase_list[self.letter].lower()     #Temporarily makes the character lower to find it in the list
                i1 = phrase_list[self.letter]               #stores the character in a varible
                i2 = characters.index(i1) + self.num                    #finds the character in the characters list, then adds the index to the number inputed, that new character is then stored
                if i2 > 25:                                       #Checks if number goes past the amount in the list, preventing error
                    i2 -= 25
                i3 = characters[i2]                 #New character is stored in a variable then put into the list, essentially replacing the character with the new one
                phrase_list[self.letter] = i3
                phrase_list[self.letter] = phrase_list[self.letter].upper()     #Returns new character to uppercase

            elif phrase_list[self.letter].islower() == True:         #Does the same thing but leaves the character lowercase if it was
                i1 = phrase_list[self.letter]
                i2 = characters.index(i1) + self.num
                if i2 > 25:
                    i2 -= 25
                i3 = characters[i2]
                phrase_list[self.letter] = i3



            self.letter += 1        #adds 1 to letter in order to iterate through the list
            copy_phrase = ''.join(phrase_list)     #makes the list into a string
        return copy_phrase


encr = Encrypter(line, numba, key)        #Calls class

if "file" in line and len(line) == 4:              #If you want to encrypt a file you can type 'file'
    line = input("What is the name of the file you want to encrypt: ")
    with open(line, 'r') as origin, open('copy.txt', 'w') as copy:      #Opens the file and creates the encrypted file
        f_line = origin.readline()
        while f_line != '':                           #Reads the file to the end
            line = f_line
            encr = Encrypter(line, numba, key)         #Repeatedly calls the class to update the line
            copy.write(encr.caesar())
            f_line = origin.readline()                  #Goes to the next line
    print("Encrypted.")
else:
    print(encr.caesar())

#Todo: add random cypher
#Todo: add password for random cypher
#Todo: add terminal clearer
#Todo: add decrypter