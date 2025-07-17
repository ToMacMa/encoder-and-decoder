import os,json
import urllib.request

def downloadFileIfNone(url,path):
    tmp = os.listdir()
    if path not in tmp:
        urllib.request.urlretrieve(url, filename=path)
downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/createCode.py","createCode.py")
try:
    from createCode import *
except:
    print("Run this program again.")
    quit()

CHAR_LIST = []
def encode():
    pass

def decode():
    pass

files = os.listdir()

downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/defaultCode.json",'defaultCode.json')
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
