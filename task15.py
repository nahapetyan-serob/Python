print ('Insert your plaintext')
text = input()
def caesar_sipher (plaintext):
    caesar_sipher = ''
    for i in range (len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i] in 'abc' or plaintext[i] in 'ABC':
                caesar_sipher += chr(ord(plaintext[i]) + 23)
            else:
                caesar_sipher += chr(ord(plaintext[i]) - 3)
        else:
            caesar_sipher += plaintext[i]
    return (caesar_sipher)
print (caesar_sipher (text))
