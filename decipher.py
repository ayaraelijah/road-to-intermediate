alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Get user input for the various variables

direction = input("Type 'Encode' to encrypt, Type 'Decode' to decrypt \n ").lower()
text = input("Type your message:\n").upper()
shift = int(input("Type your shift number: \n "))

if direction == "encode":
#created a function that takes the parameter of text and shift
    def encrypt(text, shift):
        
        cipher_text = ""

    #for each of the letter in the text gotten from user input
        for letter in text:

    #gets the first occurence of the letter in alphabets and assigns a postion variable to it 
            position = alphabets.index(letter)

    #where the text is in the alphabet list is then counted or taken the amount of steps the shift number gotten from the user and assigned to a variable
            new_position = position + shift

    #the new letter is then the new position where the text was added or counted to
            new_letter = alphabets[new_position]

    #then an empty string is created and added to the new letter to display the new letter the texts inputted
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")

    #call the function
    encrypt(text, shift)

if direction == "decode":

    def decrypt(text, shift):
        cipher_text = ""
        
        for letter in text:
            position = alphabets.index(letter)

            new_position = position - shift

            new_letter = alphabets[new_position]

            cipher_text += new_letter
        
        print(f"The decoded text is {cipher_text}")

    decrypt(text, shift)