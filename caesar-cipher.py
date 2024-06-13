#caesar-cipher.py
#Author: Vijay Ramkissoon

def caesarEncrypt(plaintext,key,alphabet, punctuation = {'A':'', 'B':'.', 'C': '?', 'D':'!', 'E':',', 'F':'\'','G':'\"', 'H':';', 'I':':'}):
    if key > len(alphabet):
        key = key % len(alphabet)
    
    index_list = []

    for letter in plaintext:
        if letter in alphabet:
            index_list.append(alphabet.index(letter))
        else:
            for index,value in punctuation.items():
                if value == letter:
                    index_list.append(index)

    print(index_list)
    
    shifted_list=[]

    for position in index_list:
        if type(position) is str:
            shifted_list.append(position)
        elif (position - key) < 0:
            shifted_list.append(len(alphabet) + position - key)
        else:
            shifted_list.append(position - key)

    print(shifted_list)
    
    ciphertext = ''

    for new_position in shifted_list:
        if type(position) is str:
            ciphertext = ciphertext + new_position
        ciphertext = ciphertext + alphabet[new_position]

    print(ciphertext)


english_alphabet = ['a','b','c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
english_punctuation = {'a':'', 'b':'.', 'c': '?', 'd':'!', 'e':',', 'f':'\'','g':'\"', 'h':';', 'i':':'}

#Test 1
p1 = 'def'
k1 = 3
caesarEncrypt(p1,k1,english_alphabet)

#Test2
p2 = 'abc'
k2 = 3
caesarEncrypt(p2,k2,english_alphabet)

#Test3
p3 = 'attack left flank at noon'
k3 = 532
caesarEncrypt(p3,k3,english_alphabet)


def caesarDecrypt(ciphertext,key, alphabet, punctuation = {'1':'', '2':'.', '3': '?', '4':'!', '5':',', '6':'\'','7':'\"', '8':';', '9':':'}):
    if key < len(alphabet):
        key = key % len(alphabet)
    
    index_list = []
    for letter in ciphertext:
        if letter in alphabet: 
            index_list.append(alphabet.index(letter))
        else:
            for pair in punctuation.items():
                index,value = pair
                if letter == index:
                    index_list.append(value)
    
    print(index_list)

    shifted_list = []
    for position in index_list:
        if (position + key) >= len(alphabet):
            shifted_list.append(position + key - len(alphabet))
        else:
            shifted_list.append(position + key)
    
    print(shifted_list)

    plaintext = ''
    for new_position in shifted_list:
        plaintext = plaintext + alphabet[new_position]
    
    print(plaintext)


#Test1
c1 = 'abc'
caesarDecrypt(c1,k1,english_alphabet)

#Test2
c2 = 'xyz'
caesarDecrypt(c2,k2,english_alphabet)