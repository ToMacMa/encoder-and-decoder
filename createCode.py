from random import *
import json
def createCode():
    out = []
    CHAR_LIST = []
    rat = []
    for i in range(32,127):
        CHAR_LIST.append(chr(i))
        rat.append(chr(i))
    out.append(rat)
    shuffle(CHAR_LIST)
    out.append(CHAR_LIST)
    return out