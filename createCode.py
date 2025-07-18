from random import *
import json
def createCode():
    out = []
    CHAR_LIST = []
    rat = []
    for i in range(32,127):
        CHAR_LIST.append(chr(i))
        rat.append(chr(i))
    CHAR_LIST.append('/n')
    rat.append('/n')
    out.append(rat)
    shuffle(CHAR_LIST)
    out.append(CHAR_LIST)
    return out
if __name__ == '__main__':
    code = createCode()
    f = open('defaultCode.json','w')
    f.write(json.dumps(code,indent=1))
    f.close()