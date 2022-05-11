import numpy as np
import base64
from math import sqrt

SAMP_RATE = 24e3
MAX_LEN = 256000

FREQ_HIGH = 5e3
FREQ_LOW = 1e3

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

def fm_encode(morse):
    timings = []
    freq = []
    cur = morse[0]

    for i in range(len(morse[1::])):
        new = morse[i]
        if new != "_" and cur != "_" and new != " " and cur != " " and i != 0:
            freq += [FREQ_LOW] * int(TIMING_DOT * SAMP_RATE / 2)
        if new == ".":
            freq += [FREQ_HIGH] * int(TIMING_DOT * SAMP_RATE)
        elif new == "-":
            freq += [FREQ_HIGH] * int(TIMING_DASH * SAMP_RATE)
        elif new == "_":
            if i != len(morse[1::]):
                if morse[i+1] != " ":
                    freq += [FREQ_LOW] * int(TIMING_SEP_LETTER * SAMP_RATE)
        elif new == " ":
            freq += [FREQ_LOW] * int(TIMING_SPACE * SAMP_RATE)
        cur = new

    freqs_diff = [ ((2*np.pi) / SAMP_RATE) * f for f in freq ]
    phases = np.concatenate(([0.0, freqs_diff[0]], freqs_diff)).cumsum()
    angles = (phases + np.pi) % (2 * np.pi) - np.pi
    iqs = np.exp(1j*angles)
    return iqs

def main():

    msg = "CAN I GET THE FLAG"
    signal = np.array(fm_encode(morse_encode(msg)), dtype = np.complex64)

    with open("signal2.iq", "wb") as f:
        f.write(signal)

    b64 = base64.b64encode(signal).decode()
    print(b64)

main()

# python3 sol.py > sig.b64.txt
# nc challenges.france-cybersecurity-challenge.fr 2252 < sig.b64.txt
# FCSC{490b88345a22d35554b3e319b1200b985cc7683e975969d07841cd56dd488649}
