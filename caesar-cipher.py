#caesar-cipher.py
#Author: Vijay Ramkissoon

def caesarEncrypt(plaintext,key,alphabet):
    if key > len(alphabet):
        key = key % len(alphabet)
    
    index_list = []

    for letter in plaintext:
        index_list.append(alphabet.index(letter))
    print(index_list)
    
    shifted_list=[]

    for position in index_list:
        if (position - key) < 0:
            shifted_list.append(len(alphabet) + position - key)
        else:
            shifted_list.append(position - key)

    print(shifted_list)
    
    ciphertext = ''

    for new_position in shifted_list:
        ciphertext = ciphertext + alphabet[new_position]

    print(ciphertext)


english_alphabet = ['a','b','c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Test 1
p1 = 'def'
k1 = 3
caesarEncrypt(p1,k1,english_alphabet)

#Test2
p2 = 'abc'
k2 = 3
caesarEncrypt(p2,k2,english_alphabet)

#Test3
#p3 = 'attack left flank at noon'
#k3 = 532
#caesarEncrypt(p3,k3,english_alphabet)


def caesarDecrypt(ciphertext,key,alphabet):
    if key < len(alphabet):
        key = key % len(alphabet)
    
    index_list = []
    for letter in ciphertext: 
        index_list.append(alphabet.index(letter))
    
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