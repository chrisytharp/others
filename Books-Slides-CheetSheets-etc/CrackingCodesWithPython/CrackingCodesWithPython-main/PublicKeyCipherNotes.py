#
# Symmetric key = one key encrypts\decrypts
# Asymetric key = two keys (Public Key Encrypts- Private Key Decrypts)
#
# RSA uses Large Prime Numbers (hundresd of digits long) in it's algo
#
# Public Key Algo = creates 2 Randomly gen Large Prime Numbers, Then Uses complicated math (including finding modular inverse)
#          to create Public & Private Keys
#
# Encryptioon helps with Condfidentiallity
# But authentication is provided by PKI (Public Key Infrastructure)
#       need this, because if ... the Gov sends you a message w/ their public key to encrypt your data w/ and send it to them
#                   How Can you verify this is really the Govt???? DIGITAL SIGNATURES
#
# DIGITAL SIGNATURES: allow us to electronically sign documents using Encryption
#  RSA Cipher (& other Public Key Ciphers) not only encrypts BUT allows us to DIGITALLY SIGN a File /or/ String
#   example, Alica can encrypt a message with her PRIVATE key, which produces cipherText, (only her PUBLIC Key can decrypt this ciphertext)
#           This cipherText becomes Alica's DIGITAL SIGNATURE!!!    This ISN'T a secret because her PUBLIC key can decrypt this cipherText.
#           (By encrypting a message w/ her PRIVATE KEY, alica can digitally sign a message that can't be FORGED) Because Alica is the
#           only one with her private key, this guarantees that Alica wont be able to DENY authoring that message a.k.a NON-REPUDIATION!!!
#
#   DIGITAL SIGNATURES are used for: authentication of Public Keys,! cryptocurrency,! & even Anonymous Web Surfing
#
# MITM Attack
# NOTE: Public Key CIPHERS only provides Confidentiality and NOT authentication



#       Public Key is 2 numbers 'n' & 'e'
#       Private Key is 2 numbers 'n' & 'd'
#
# 3 steps to create these Numbers:
#   (1)- Create 2 random, distinct, very Large Prime Numbers 'p' & 'q'
#               then multiply 'p' & 'q' to get a number called 'n'                               p * q = n
#   (2)- Create a Random Number called 'e' which is 'Relativley Prime' to (p -1) x (q -1)     (Relative Prime is Two integers are relatively prime (or coprime) if there is no integer #                                                                                                                                                  greater than one that divides them both )
#   (3)- Calculate the modular inverse of 'e' which we'll call 'd'
#                        GET Modular Invers of 2 numbers is represented by
#                                                                (a*i) % m ==1
#
# Notice 'n' is used in both Keys. The 'd' num MUST be kept sceret cause it can DECRYPT messages.
#
# we use 1024 to speed up process but in reality 2048 bits and 3072 bits is neccessary for secure public key encryption

Public Cipher converts multiple characters into one integer called a BLOCK & then encrypts one block at a time.
	a BLOCK is a arger integer that represents a fixed numberof text characters
Converting a String into a Block: 

Mathmatics of Public Key Cipher Encryption & Decryption:

	Encrypt each integer BLOCK with  C = M(to the power of e) mod n
	Decrypt each integer BLOCK with  M = C(to the power of d) mod n
