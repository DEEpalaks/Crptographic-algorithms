def find_inverse(n,value):
    result=-1
    for i in range(1,value+1):
        if(n*i-1)%value==0:
            result=i;
            break;
    return result;
def affine_encryption(plain,key_a,key_b):
    plain_1=plain.upper()
    cipher=""
    for i in plain_1:
        cipher+=chr(((ord(i)-65)*key_a+key_b)%26+65)
    return cipher
def affine_decryption(cipher,key_a,key_b):
    cipher_1=cipher.lower();
    plain=""
    inverse=find_inverse(key_a,26)
    for i in cipher_1:
        plain+=chr((ord(i)-97-key_b)*inverse%26+97)
    return plain
if __name__=="__main__":
    plain=input("Enter the plain text..........")
    list_1=[1,3,5,7,9,11,15,17,19,21,23,25]
    key_b=int(input("Enter b value in range 0 to 25.........."))
    key_a=int(input("Enter the a value.........."))
    while(key_a not in list_1):
        print("Key value a is not valid key...kindly enter the valid key value again..........")
        key_a=int(input("Enter the a value.........."))
    cipher=affine_encryption(plain,key_a,key_b)
    print("After encryption the cipher text is..........",cipher)
    plain=affine_decryption(cipher,key_a,key_b)
    print("After decryption the plain text is..........",plain)
