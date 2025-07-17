import os,json

files = os.listdir()

if 'defaultCode.json' not in files:
    f = open('defaultCode.json','w')
    f.write('{"code":"helloWorld!"}')
    f.close()
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