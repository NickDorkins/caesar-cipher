# Create an encrypt function that takes in a plain text phrase and a numeric shift.
    # the phrase will then be shifted that many letters.
    

def encrypt(string, shift):
    # Assign empty string to capture post shift message
    message = "" 

    # Clean the shift number before running it through the code block
    # Account for 0 shifts and negative inputs
    key = shift % 26
    if key == 0:
        return('Invalid shift key')
    if key < 0:
        key = key + 26
        if key == 0:
            return('Invalid shift key')
    print('key:', key)

    # Establish length of input string
    mes_len = len(string)

    # for loop over the string to look at each character
    for letter in range(0, mes_len):
        
        # Convert letter to ASCII numerical value
        numeric = ord(string[letter])
        # print('numeric', numeric)

        # Account for spaces
        if numeric == 32:
            encrypted = numeric
            # print('encrypted == 32 statement', encrypted)
        else:    
            # Add the input shift amount to the ASCII value
            encrypted = numeric + key
            # print('encrypted + key', encrypted)

        # Check values to ensure that they are within the range that we would like (65-90:Uppercase and 97-122:Lowercase)
        if numeric >= 65 and numeric <= 90:
            if encrypted < 65: 
                encrypted = encrypted + 26
                # print('Under65:', encrypted)
            elif encrypted > 90:
                encrypted = encrypted - 26
                # print('Over90', encrypted)

        if numeric >= 97 and numeric <= 122:
            if encrypted < 97:
                encrypted = encrypted + 26
                # print('Under97', encrypted)
            elif encrypted > 122: 
                encrypted = encrypted - 26
                # print('Over122', encrypted)
            
            # if (encrypted > 65 and encrypted < 90) or (encrypted > 97 and encrypted < 122): 
        message = message+chr(encrypted)

    return message

# print(encrypt('hello', 1))
# print(encrypt('JeLlO', 27))
# print(encrypt('ALL CAPITAL LETTERS ZZZ', 100))
# print(encrypt('all lowercase letters zzz', -100))
print(encrypt('It was the best of times, it was the worst of times.', 1))
    
# Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

def decrypt(encrypted, key):
    readable_text = encrypt(encrypted, -key)
    return readable_text

   
# print('Decrypt', decrypt('EPP GETMXEP PIXXIVW DDD', -100))

# create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.





# Devise a method for the computer to determine if code was broken with minimal human guidance.