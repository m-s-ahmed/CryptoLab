import string 

#define a function that do -> take letters only , convert uppercase , i->j
#take the parameter s as a string
def sanitize(s):
    out=[]
    for ch in s:
        if ch.isalpha():
            ch=ch.upper()
            if ch=="I":
                ch="J"
            out.append(ch)
    return "".join(out)

#define another function that create matrix
def make_matrix(key):
    used=set(["I"])
    seq=[]

    key=sanitize(key)

    for ch in key:
        if ch not in used:
            used.add(ch)
            seq.append(ch)
    
    for ch in string.ascii_uppercase:
        if ch not in used:
            used.add(ch)
            seq.append(ch)

    mat=[seq[i:i+5] for i in range(0,25,5)]

    pos={}

    for r in range(5):
        for c in range(5):
            pos[mat[r][c]]=(r,c)
    
    return mat,pos

#define function for print the matrix
def print_matrix(mat):
    print("\nMatrix (I/J combined -> J kept)")
    for row in mat:
        print(" ".join(row))
    print()

#define function for prepare the plaintext
def prepare_plaintext(text):
    s=sanitize(text)
    res=[]
    i=0
    while i<len(s):
        a=s[i]
        b=s[i+1] if i+1<len(s) else None

        if b is None:
            res.append(a)
            break
        if a==b:
            res.append(a)
            res.append("X")
            i+=1
        else:
            res.append(a)
            res.append(b)
            i+=2
        
    if len(res)%2 != 0:
        res.append("X")

    return "".join(res)

#make a function for processing 
def process(text,mat,pos,encrypt=True):
    step=1 if encrypt else -1
    out=[]

    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        r1,c1=pos[a]
        r2,c2=pos[b]

        if r1 == r2:  # same row
            out.append(mat[r1][(c1 + step) % 5])
            out.append(mat[r2][(c2 + step) % 5])

        elif c1 == c2:  # same column
            out.append(mat[(r1 + step) % 5][c1])
            out.append(mat[(r2 + step) % 5][c2])

        else:  # rectangle
            out.append(mat[r1][c2])
            out.append(mat[r2][c1])
    
    return "".join(out)

#make function for remove filler character in the middle and also last
def remove_filler_x(text):
    temp=[] #keep here the final clean text
    n=len(text)
    for i in range(n):
        #as i not the first and last character 
        if 0<i<n-1 and text[i]=="X" and text[i-1]==text[i+1]:
            continue
        temp.append(text[i])
    #temp not empty and last character X
    if temp and temp[-1]=="X":
        temp.pop()
    
    return "".join(temp)


#-------------Main Function------------#
key=input("Key: " ).strip()
mat,pos=make_matrix(key)
print_matrix(mat)

while True:
    cmd=input("EN/DE/EX:").strip().upper()

    if cmd=="EN":
        msg=input("Message")
        p=prepare_plaintext(msg)
        c=process(p,mat,pos,encrypt=True)
        print("Encrypted: ",c,"\n")

    elif cmd == "DE":
        cipher = input("Cipher: ")
        c = sanitize(cipher)
        if len(c) % 2 != 0:
            print("Invalid ciphertext length (must be even).\n")
            continue
        p = process(c, mat, pos, encrypt=False)
        p = remove_filler_x(p)
        print("Decrypted:", p, "\n")

    elif cmd == "EX":
        break
    
    else:
        print("Invalid command.\n")

