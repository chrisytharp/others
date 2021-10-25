# Modulo Operator (%) aka mod  | returns the remainder | i.e. 10 mod(%) 8 = 2
#
# Ceaser Cipher = addiion to Encrypt (will need a wraparound solution) / subtraction to Decrypt
#
# Multiplicative Cipher = multiple the index of char (will need wrap wraparound solution) with key and mod that by the "symbole set size"
#                       Multiplicative Cipher reqs. KEY [num1] & Symbol Set Size[num2] to be relatively prime "coprime" | GCD(num1, num2) == 1 |
#                                   NOTE: num1 and num2 NEED to be coprime but DONT need to be Prime Numbers
#                                       Coprime numbers are 2 number where the GCD is 1
#
# Example of Encrypting Multiplicative Cipher          Plaintext * Key % len()ofSymboleSet = CipherText
#           symbole set len() == 66
#           Lets Encrypt "Cat" using Key53
#                                           C is at index 2  ->  2*53 = 106 % 66 = 40     index[40] in symbol set = o
#                                           a is at index 26 ->  26*53 = 1378 % 66 = 58   index[58] in symbol set = 7
#                                           t is at index 45 ->  45*53 =  2385 % 66 = 9   index[9]  in symbol set = J
#           "Cat" encrypted with key 53 with symbol set size of 66 =  'o7J'
#
#Example of Decrypting Multiplicative Ciphertext       CipherText * modular Inverse of Key % len()ofSymboleSet = Plaintext
#
#           Multiply the modular inverse of the Key Used '53' by the len() of synbole set size '66'
#              key % symbol set = modular inverse   -> 53 % 66 = 5
#                                           o is at index 40  ->  40 * 5 % 66 = 2       index[2]  in symbol set = C
#                                           7 is at index 58  ->  58 * 5 % 66 = 7       index[7]  in symbol set = a
#                                           J is at index 9   ->  9  * 5 % 66 = 45      index[45] in symbol set = t
#
#Affine Cipher = Utilizes the Multiplicative Cipher and then Ceaser Cipher
#        Encrypt
#               [[Reqs 2 KEYS & a mod]] KeyA = integer you multiple the char index in symbol set
#                                       KeyB = integer that you add to "product" after KeyA is completed you add KeyB
#                                        mod = integer of the total size of "Symbol Size" after KeyB is added you mod that to get the cipherText index char
#
#               Plaintext[index # in symbole set] -> Multiply by KeyA -> Add KeyB -> mod by symbole set size -> Ciphertext [index # in symbol set]
#
#       Decrypt
#               Modular Invers of 2 numbers is represented by
#                                                                (a*i) % m ==1
#                                                                 i = modular inverse
#                                                                 a = Key
#                                                                 m = symbol set size
#                                                          ex..
#                                                                   modular inverse of   5 mod 7
#                                                       (5*i) % 7 == 1
#                                                                       can brute force by replacing "i" with 1,2,3,4,5 until the "modular inverse" is found
#                                       (5*3) % 7 ==1   ->  15 % 7 == 1   ->  1 == 1
#
#               Ciphertext[index # in symbol set] -> Subtract KeyB -> Multiple by "mod inverse" of KeyA -> mod by symbol set size -> Plaintext [index # in symbol set]
#

#
#
#
#
