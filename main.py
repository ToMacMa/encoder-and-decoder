import os,json
import urllib.request
from createCode import *

CHAR_LIST = []

def setupListForFunctions(code):
    for i in range(32,127):
        CHAR_LIST.append(chr(i))

setupListForFunctions(1)
print(CHAR_LIST)

def encode():
    pass

def decode():
    pass

files = os.listdir()

if 'defaultCode.json' not in files:
    url = "https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/defaultCode.json"
    filename, headers = urllib.request.urlretrieve(url, filename="defaultCode.json")
files = os.listdir()

def readCode():
    files = os.listdir()
    if 'code.json' not in files:
        f = open('defaultCode.json','r')
        code = json.load(f)
        f.close()
        return code
    else:
        f = open('code.json','r')
        code = json.load(f)
        f.close()
        return code
code = readCode()
