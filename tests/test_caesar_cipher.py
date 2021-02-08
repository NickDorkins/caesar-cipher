from caesar_cipher.caesar_cipher import encrypt, decrypt

# ------------------------------------------------------------

# encrypt a string with a given shift
def test_encrypt_a_string_with_a_given_positive_shift():
   encrypted = encrypt('ALL CAPITAL LETTERS ZZZ', 100)
   actual = encrypted
   expected = 'WHH YWLEPWH HAPPANO VVV'
   assert actual == expected

def test_encrypt_a_string_with_a_given_negative_shift():
   encrypted = encrypt('ALL CAPITAL LETTERS ZZZ', -100)
   actual = encrypted
   expected = 'EPP GETMXEP PIXXIVW DDD'
   assert actual == expected

# ------------------------------------------------------------

# decrypt a previously encrypted string with the same shift
def test_decrypt_a_previously_encrypted_string_with_known_shift():
    decrypted = decrypt('EPP GETMXEP PIXXIVW DDD', -100)
    actual = decrypted
    expected = 'ALL CAPITAL LETTERS ZZZ'
    assert actual == expected

def test_decrypt_a_previously_encrypted_string_with_known_shift():
    encrypted = encrypt('Hello', -100)
    decrypted = decrypt(encrypted, -100)
    actual = decrypted
    expected = 'Hello'
    assert actual == expected

# ------------------------------------------------------------


# encryption should handle upper and lower case letters
def test_encrypt_handle_upper_and_lower_case_letters():
    encrypted = encrypt('It was the best of times, it was the worst of times.', 1)
    actual = encrypted
    expected = 'Ju xbt uif cftu pg ujnft- ju xbt uif xpstu pg ujnft/'
    assert actual == expected

# ------------------------------------------------------------

# encryption should allow non-alpha characters but ignore them, including white space




# ------------------------------------------------------------


# decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.








# print(encrypt('hello', 1))
# print(encrypt('JeLlO', 27))
# print(encrypt('ALL CAPITAL LETTERS ZZZ', -100))
# print(encrypt('all lowercase letters zzz', -100))
# print(encrypt('It was the best of times, it was the worst of times.', 1))
