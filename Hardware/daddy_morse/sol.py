import numpy as np
import base64
from math import sqrt

SAMP_RATE = 24e3
MAX_LEN = 256000

FREQ = 5e3

TIMING_DOT = 1/1000
TIMING_DASH = 5/1000
TIMING_SEP_LETTER = 5/1000
TIMING_SPACE = 20/1000

alphabet = { 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

def morse_encode(msg):
    res = ""
    for word in msg.split(" "):
        for letter in word:
            if letter in alphabet:
                res += alphabet[letter]
            elif letter == "":
                continue
            else:
                return "error"
            res += "_"
        res += " "
    return res

def am_encode(morse):
    iqs = []
    cur = morse[0]

    for i in range(len(morse[1::])):
        new = morse[i]
        if new != "_" and cur != "_" and new != " " and cur != " " and i != 0:
            nb = int(TIMING_DOT * SAMP_RATE)
            iqs += [0j] * nb
        if new == ".":
            nb = int(TIMING_DOT * SAMP_RATE)
            iqs += [1+1j] * nb
        elif new == "-":
            nb = int(TIMING_DASH * SAMP_RATE)
            iqs += [1+1j] * nb
        elif new == "_":
            if i != len(morse[1::]):
                if morse[i+1] != " ":
                    nb = int(TIMING_SEP_LETTER * SAMP_RATE)
                    iqs += [0j] * nb
        elif new == " ":
            nb = int(TIMING_SPACE * SAMP_RATE)
            iqs += [0j] * nb
        cur = new

    return iqs

def main():
    msg = "CAN I GET THE FLAG"
    signal = np.array(am_encode(morse_encode(msg)), dtype = np.complex64)

    with open("signal2.iq", "wb") as f:
        f.write(signal)

    b64 = base64.b64encode(signal).decode()
    print(b64)

main()
    
# python3 sol.py > sig.b64.txt
# nc challenges.france-cybersecurity-challenge.fr 2251 < sig.b64.txt
# FCSC{e8b4cad7d00ca921eb12824935eea3b919e5748264fe1c057eef4de6825ad06c}
