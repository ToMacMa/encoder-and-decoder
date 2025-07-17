import os,json
import urllib.request

files = os.listdir()

if 'defaultCode.json' not in files:
    url = "https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/defaultCode.json"
    print ("download start!")
    filename, headers = urllib.request.urlretrieve(url, filename="defaultCode.json")
    print ("download complete!")
    print ("download file location: ", filename)
    print ("download headers: ", headers)
files = os.listdir()

def readCode():
    files = os.listdir()
    if 'code.json' not in files:
        f = open('defaultCode.json','r')
        code = json.load(f)
        f.close()
        return code['code']
    else:
        f = open('code.json','r')
        code = json.load(f)
        f.close()
        return code['code']
code = readCode()

print(code)