import random
import math
import time
import string

# ------------------ Helpers ------------------

def onlyLettersUpper(s):
    return ''.join(ch.upper() for ch in s if ch.isalpha())


def decryptWithKey(cipher, key):
    out = ""
    for ch in cipher:
        if ch.isalpha():
            ch = ch.upper()
            out += chr(ord('A') + key[ord(ch) - ord('A')])
        else:
            out += ch
    return out


# ------------------ Scoring ------------------

def scoreText(plain):

    L = [
        2.6, 0.5, 0.9, 1.3, 3.0, 0.6, 0.7, 1.0, 2.3, 0.1,
        0.3, 1.5, 0.8, 2.0, 2.2, 0.7, 0.1, 2.0, 1.9, 2.4,
        0.8, 0.3, 0.4, 0.2, 0.6, 0.1
    ]

    BIG = {
        "TH":3.5,"HE":3.2,"IN":2.8,"ER":2.6,"AN":2.6,"RE":2.4,"ON":2.4,
        "AT":2.3,"EN":2.2,"ND":2.2,"TI":2.0,"ES":2.0,"OR":2.0,"TE":1.9,
        "OF":1.9,"ED":1.8,"IS":1.8,"IT":1.8,"AL":1.7,"AR":1.7,"ST":1.7,
        "TO":1.7,"NT":1.6,"NG":1.6,"SE":1.5,"HA":1.5,"AS":1.5,"OU":1.4,
        "IO":1.2,"LE":1.2,"VE":1.2
    }

    TRI = {
        "THE":6.0,"AND":5.0,"ING":4.5,"HER":3.7,"ERE":3.2,"ENT":3.2,"THA":3.0,
        "NTH":2.8,"WAS":2.6,"ETH":2.6,"FOR":2.5,"HAT":2.5,"HIS":2.4,"ION":2.4,
        "TIO":2.3,"VER":2.2,"TER":2.2,"RES":2.1,"EST":2.1,"ATI":2.1,"OTH":2.0
    }

    WORDS = {
        "THE","AND","TO","OF","IN","IS","IT","THAT","FOR","ON","WITH","AS","WAS","BE","ARE",
        "THIS","HAVE","FROM","OR","ONE","HAD","NOT","BY","BUT","WHAT","ALL","WERE","WHEN","WE"
    }

    sc = 0.0
    t = onlyLettersUpper(plain)

    # 1) letter preference
    for c in t:
        sc += L[ord(c) - ord('A')]

    # 2) bigrams
    for i in range(len(t) - 1):
        bg = t[i:i+2]
        if bg in BIG:
            sc += BIG[bg]

    # 3) trigrams
    for i in range(len(t) - 2):
        tg = t[i:i+3]
        if tg in TRI:
            sc += TRI[tg]

    # 4) word bonus
    w = ""
    for ch in plain:
        if ch.isalpha():
            w += ch.upper()
        else:
            if w and w in WORDS:
                sc += 8.0 + len(w)
            w = ""
    if w and w in WORDS:
        sc += 8.0 + len(w)

    # 5) penalty: Q not followed by U
    for i in range(len(t)):
        if t[i] == 'Q':
            if i + 1 >= len(t) or t[i+1] != 'U':
                sc -= 8.0

    return sc


# ------------------ Initial Key ------------------

def initialKeyByFrequency(cipher):
    t = onlyLettersUpper(cipher)
    freq = [0] * 26

    for c in t:
        freq[ord(c) - ord('A')] += 1

    idx = list(range(26))
    idx.sort(key=lambda x: freq[x], reverse=True)

    EN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    key = [0] * 26
    for rank in range(26):
        cipherL = idx[rank]
        key[cipherL] = ord(EN[rank]) - ord('A')

    return key


def swapRandom(key):
    a = random.randint(0, 25)
    b = random.randint(0, 25)
    while b == a:
        b = random.randint(0, 25)
    key[a], key[b] = key[b], key[a]


def printKey(key):
    print("\nKey mapping (cipher -> plain):")
    print("CIPHER:", end=" ")
    for i in range(26):
        print(chr(ord('A') + i), end=" ")
    print("\nPLAIN :", end=" ")
    for i in range(26):
        print(chr(ord('A') + key[i]), end=" ")
    print()


# ------------------ Main ------------------

print("Paste ciphertext. Type END on a new line to finish:")

cipher = ""
while True:
    line = input()
    if line == "END":
        break
    cipher += line + "\n"

base = initialKeyByFrequency(cipher)

random.seed(time.time())

bestKey = base[:]
bestPlain = decryptWithKey(cipher, bestKey)
bestScore = scoreText(bestPlain)

RESTARTS = 5
STEPS = 30000

print("Working...")

for r in range(RESTARTS):

    cur = base[:]

    for _ in range(60):
        swapRandom(cur)

    curPlain = decryptWithKey(cipher, cur)
    curScore = scoreText(curPlain)

    T = 20.0

    for step in range(STEPS):

        nxt = cur[:]
        swapRandom(nxt)

        nxtPlain = decryptWithKey(cipher, nxt)
        nxtScore = scoreText(nxtPlain)

        if nxtScore > curScore:
            cur = nxt
            curScore = nxtScore
            curPlain = nxtPlain
        else:
            prob = math.exp((nxtScore - curScore) / T)
            if random.random() < prob:
                cur = nxt
                curScore = nxtScore
                curPlain = nxtPlain

        T *= 0.99995
        if T < 0.05:
            T = 0.05

        if curScore > bestScore:
            bestScore = curScore
            bestKey = cur[:]
            bestPlain = curPlain

    print(f"Restart {r+1}/{RESTARTS} done. BestScore={bestScore}")

print("\n================ BEST DECRYPTION ================")
print(bestPlain)
printKey(bestKey)