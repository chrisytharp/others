#
#       Public Key is 2 numbers 'n' & 'e'
#       Private Key is 2 numbers 'n' & 'd'
#
# 3 steps to create these Numbers:
#   (1)- Create 2 random, distinct, very Large Prime Numbers 'p' & 'q'
#               then multiply 'p' & 'q' to get a number called 'n'                               p * q = n
#   (2)- Create a Random Number called 'e' which is 'Relatively Prime' to (p -1) x (q -1)
#   (3)- Calculate the modular inverse of 'e' which we'll call 'd'

# Notice 'n' is used in both Keys. The 'd' num MUST be kept sceret cause it can DECRYPT messages.
#
#
# Public Key Gen

import os, random, sys, primeNum, cryptoMath

def main():
    # Create a public/ private keypair with 1024-bit key
    print('Making key files...')
    makeKeyFiles('textBook', 1024)
    print('Key Files made')

def generateKey(keySize):
    #  Create public\private keys 'keySize' bits in size
    p = 0
    q = 0
    # Step 1: Create 2 prime numbers 'p & q' Calculate n = p *q
    print("Generating 'p' prime ...")
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p * q

    # Step 2: Create number 'e' that is relatively Prime to (p-1)*(q-1):
    print("Generating 'e' that is relatively prime to (p-1)*(q-1)...")
    while True:
        # keep trying random numbers for 'e' until one is valid:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p - 1) * (q -1)) == 1:
            break

    # step 3: Calculate 'd' the mod inverse of 'e'
    print("Calculating 'd' that is mod inverse of 'e'...")
    d = cryptoMath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public Key:', publicKey)
    print('Private Key:', privateKey)

    return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    # Creates 2 files 'x_pubkey.txt' and 'x_privkey.txt' (where x is the value in name)
    #   w\ the n,e and d,e integers written in them, delimited by a comma
    # Our safety check will prevent us from overwriting our old key files:
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit("WARNING: the file %s_pubkey.txt or %s_privkey.txt already exists! Use different name or delete these files & rerun this program" % (name, name))

    publicKey, privateKey = generateKey(keySize)  # ex of generate keys using Multiple assignment 

    print()
    print("The public key is a %s and a %s digit number." % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print("Writing public key to file %s_pubkey.txt..." % (name))
    fo = open("%s_pubkey.txt" % (name), 'w')
    fo.write("%s, %s, %s" % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    print()
    print("The private key is a %s and a %s digit number." % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print("Writing private key to file %s_privkey.txt..." % (name))
    fo = open("%s_privkey.txt" % (name), 'w')
    fo.write("%s, %s, %s" % (keySize, privateKey[0], privateKey[1]))
    fo.close()

# If this is run (instead as imported as module) call the main() funciton
if __name__ == "__main__":
    main()






#Hence finding out the private key from public key is impossible. This is true as long as factorisation is infeasible. Using Shor's algorithm in Quantum computers, this problem actually becomes feasible. So until quantum computers are built which can solve it, RSA and other public key cryptosystems are secure.
