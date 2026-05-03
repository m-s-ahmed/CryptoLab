#define function for gcd
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

#define function for prime number
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#define function for possible_e
def possible_e(phi,limit=15):
    e_list=[]
    for e in range(2,phi):
        if gcd(e,phi)==1:
            e_list.append(e)
            if len(e_list)==limit:
                break
    return e_list

#define function for extended euclid
def egcd(a,b):
    if b==0:
        return a,1,0
    #recursive call
    g,X1,Y1=egcd(b,a%b)
    x=Y1
    y=X1-(a//b)*Y1
    return g,x,y

#define function for mod inverse
def modinv(e,phi):
    g,x,_=egcd(e,phi)
    if g!=1: #if g=1, then modulo inverse not exit
        return None
    return x%phi #if negative , then make it positive

#for encryption
def encrypt_number(m,e,n):
    return pow(m,e,n)

#for decryption
def decrypt_number(c,d,n):
    return pow(c,d,n)

print("----RSA----")

p=int(input("Enter prime p: "))
q=int(input("Enter prime q: "))

if(not is_prime(p)) or (not is_prime(q)) or (p==q):
    print("p and q must be prime number")
    quit()

n=p*q
phi=(p-1)*(q-1)

print("\n-- Values --")
print("n = ",n)
print("phi = ",phi)

e_list=possible_e(phi,limit=15)

print("\n Choose e from below: ")
for i, e in enumerate(e_list,1):
    print(f"{i}) {e}")

idx=int(input("Select a (serial) : "))

if idx<1 or idx>len(e_list):
    print("Invalid Selection!")
    quit()

#determine e and d value
e=e_list[idx-1]
d=modinv(e,phi)

if d is None:
    print("d not found, choose another e.")
    quit()

print("\n ---Keys---")
print("Public: (e,n) =",(e,n))
print("Private: (d,n) =",(d,n))

print("\n1) Text Encrypt/Decrypt")
print("2) Number Encrypt/Decrypt")
choice = input("Choose (1/2): ").strip()

if choice=="2":
    m=int(input("Enter number m (<n): "))
    if m>=n:
        print("m must be < n")
        quit()

    c=encrypt_number(m,e,n)
    print("Cipher: ",c)

    m2=decrypt_number(c,d,n)
    print("Decrypted:",m2)

elif choice == "1":
    msg = input("Enter text: ")

    cipher = []
    for ch in msg:
        #convert each character to its unicode point. ascii is a subset of unicode,having range 0-127
        m = ord(ch)
        if m >= n:
            print("Character too big for chosen n. Use bigger primes.")
            quit()
        cipher.append(encrypt_number(m, e, n))

    print("Cipher:", cipher)

    plain = ""
    for c in cipher:
        #convert unicode to character again
        plain += chr(decrypt_number(c, d, n))
    print("Decrypted:", plain)

else:
    print("Invalid choice!")  


