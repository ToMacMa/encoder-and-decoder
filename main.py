import os,json
import urllib.request

def downloadFileIfNone(url=str(),path=str()):
    """Downloads a file/folder if it isn't already present."""

    tmp = os.listdir()
    if path not in tmp:
        urllib.request.urlretrieve(url, filename=path)
def encode(code=list(),text=str()):
    output = ""
    text = str(text)
    code0 = code[0]
    code1 = code[1]
    for i in text:
        output += code1[code0.index(i)]
    return output


def decode(code,text):
    output = ""
    text = str(text)
    code0 = code[0]
    code1 = code[1]
    for i in text:
        output += code0[code1.index(i)]
    return output

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

def encodeFile(code,fp,backup=True):
    """fp - file path \n 
       backup - True by default, makes a backup of the original file. 
    """
    f = open(fp,'r')
    data = f.read()
    f.close()
    f = open(f"{fp}.encodebackup",'w')
    f.write(data)
    f.close()
    f = open(fp,'w')
    data = encode(code,data)
    f.write(data)
    f.close()

def decodeFile(code,fp,backup=True):
    """fp - file path \n 
       backup - True by default, makes a backup of the original file. 
    """
    f = open(fp,'r')
    data = f.read()
    f.close()
    f = open(f"{fp}.decodebackup",'w')
    f.write(data)
    f.close()
    f = open(fp,'w')
    data = decode(code,data)
    f.write(data)
    f.close()

def loadSettings():
    f = open('settings.json','r')
    settings = json.loads(f.read())
    f.close()
    return settings
def loadLanguage(settings):
    f = open(f"{settings['lang']}.json")
    langData = json.loads(f.read())
    f.close()
    return langData

downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/database-languages/refs/heads/main/encdecoder/en_us.json","en_us.json")
downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/database-languages/refs/heads/main/encdecoder/pl.json","pl.json")
downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/database-languages/refs/heads/main/encdecoder/defaults.json","settings.json")
settings = loadSettings()
langData = loadLanguage(settings)

if __name__ == "__main__":
    downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/createCode.py","createCode.py")
    try:
        from createCode import *
    except:
        print(langData['error1'])
        quit()

    CHAR_LIST = []
    files = os.listdir()

    downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/defaultCode.json",'defaultCode.json')
    files = os.listdir()

    code = readCode()

    match input(langData['prompt1']):
        case "enc":
            match input(langData['prompt2']):
                case "file":
                    encodeFile(code,str(input(langData['filePath'])))
                    print("Done!")
                case "text":
                    print(encode(code,input(langData['textEncode'])))
                case _:
                    print(langData['invalid'])
            
        case "dec":
            match input(langData['prompt1']):
                case "file":
                    decodeFile(code,str(input(langData['filePath'])))
                    print("Done!")
                case "text":
                    print(code,decode(code,input(langData['textDecode'])))
                case _:
                    print(langData['invalid'])
        case _:
            print(langData['invalid'])
