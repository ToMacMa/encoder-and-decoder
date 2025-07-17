from random import *
import json
def createCode():
    CHAR_LIST = []
    for i in range(32,127):
        CHAR_LIST.append(chr(i))
    shuffle(CHAR_LIST)
    return CHAR_LIST