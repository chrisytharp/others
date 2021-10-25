# This program proves that the keyspace of the affine cipher is limited
# to less than len(SYMBOLS) ^ 2

import affineCipher, cryptoMath

message = "Make things as simple as possible, but not simple"
for keyA in range (2, 80):          # 0 and 1 are not allowed in cipher so we start at 2
    key = keyA * len(affineCipher.SYMBOLS) + 1     # the "+ 1" represents "keyB"- 'keyB' always is '1'

    if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:       #This verifies that keyA is coprime w/ len(sysmbol set) & we get the GDC for the if statement
        print(keyA, affineCipher.encryptMessage(key, message))
        
# OUTPUT- keyA = 5 & keyA = 71 these keys have the same out put., keyA = 7 & 73 are the same, keyA 13 & 79 are the same
# all 71-5=66 73-7-66 79-13=66 
# the affine Cipher has a wraparounf essect like the Caeser cipher