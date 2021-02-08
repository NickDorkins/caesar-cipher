# Create an encrypt function that takes in a plain text phrase and a numeric shift.
    # the phrase will then be shifted that many letters.
    

def encrypt(string, shift):
    # Assign empty string to capture post shift message
    message = "" 

    # Clean the shift number before running it through the code block
    if shift == 0:
        return('Invalid shift key')
    if shift >= 26:
        key = shift % 26
        if key == 0:
            return('Invalid shift key')
    else:
        key = shift
    
    print('key:', key)
    # # Establish length of input string
    mes_len = len(string)

    # for loop over the string to look at each character
    for letter in range(0, mes_len):
        
        # Convert letter to ASCII numerical value
        numeric = ord(string[letter])
        print('numeric', numeric)

        # Account for spaces
        if numeric == 32:
            encrypted = numeric
        else:    
            # Add the input shift amount to the ASCII value
            encrypted = numeric + key
            print('encrypted', encrypted)
#    Check values to ensure that they are within the range that we would like (65-90:Uppercase and 97-122:Lowercase)
      
        if encrypted < 65:
            encrypted + 26
            # print('Under65:', encrypted)
        elif encrypted > 90:
            encrypted - 26
            # print(encrypted)
        elif encrypted < 97 :
            encrypted + 26
            # print(encrypted)
        elif encrypted > 122: 
            encrypted - 26
            # print(encrypted)
            
            # if (encrypted > 65 and encrypted < 90) or (encrypted > 97 and encrypted < 122): 
        message = message+chr(encrypted)

    return message

# print(encrypt('hello', 1))
# print(encrypt('JeLlO', 27))
# print(encrypt('ALL CAPITAL LETTERS', 596))
print(encrypt('all lowercase letters', -1))
# print(encrypt('JeLlO', 596))
    
# Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.


# create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.



# Devise a method for the computer to determine if code was broken with minimal human guidance.