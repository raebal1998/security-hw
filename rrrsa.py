import math
try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass
p=0
q=0
l = []
primeList =[2,	3	,5,	7,	11,	13	,17	,19,23,29	,31	,37	,41	,43	,47	,53	,59	,61	,67,71,
	73,	79,	83,	89,	97,	101,103,107	,109,113,127,131,137,139,149,151,157,163,167,173
,	179,181,191,193	,197,199,211,223,227,229,233,239,257,263,269,271,277,281
,283,	293	,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,7853,7867,	7873,7877,7879]
e=0
def chech_prime(prime):
    if prime == 1:
        return False
    if prime == 2:
        return True
    if prime % 2 == 0:
        return False

    sqr = int(math.sqrt(prime)) + 1

    for divisor in range(3, sqr, 2):
        if prime % divisor == 0:
            return False
    return True
def get_int_prime_only(message):
    while True:
        try:
            p = int(input(message))
            while True:
                if chech_prime(p) == False:
                     print("You entered a non-prime number ")
                     p = int(input(message+' again '))
                else:
                    break
            break
        except ValueError:
            print('Please enter an integer value.')
    return p

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l


def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for : ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('No modular multiplicative inverse for :' + str(c) + '.')
    return m
def encrypt(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
def check_e():
    while True:
        e = int(input("choose e from the above list"))
        if e in l == False:
            print("You entered an invalid number  ")
        else:
            break
        return e
print("*************** Welcome to enc/decrypt messages program **********************")
print("       here you can enc/decrypt  your messages using RSA cryptosystems ")
know =input("       First Do you know what is the prime number means type ?YES/NO :")
if know.upper() =='NO':
    print('A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers Examples:')
    print(primeList)
p= get_int_prime_only('Please Enter the first prime number')
q = get_int_prime_only('Please Enter the second prime number')

print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
print("Euler's function " + str(phi) + "\n")
print("Choose an e from a below coprimes list to complete the process:\n")
print(str(coprimes(phi)) + "\n")
while True:
    e = int(input('choose e from the above list'))
    if e in l == False:
        print("You entered an invalid number  ")
    else:
        break

d = modinv(e, phi)
print("\nYour public key is:- a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is:- a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")
while True:
    try:
        func = input("Second :Do you WAnt to encrypt or decrypt type  encrypt/decrypt :")
        if any(func.isdigit() for s in func):
            raise ValueError("input supplied should be of type 'str'")
        else:
            break
    except ValueError :
        print ("please enter string only")

if func.upper() == 'ENCRYPT':
    s = input("Enter a message to encrypt: ")
    print("\nPlain message: " + s + "\n")
    some_input = s  # This input is the value separated by spaces
    for field in some_input.split():
        encryptm = encrypt(field)
        print("Your encrypted message: " + encryptm + "\n")
        dec = decrypt(encryptm)
        print("Your decrypted message: " + dec + "\n")
if func.upper() == 'DECRYPT':
    decryptm = input("Enter a message to Decrypt: ")
    dec = decrypt(decryptm)




