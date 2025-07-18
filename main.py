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



if __name__ == "__main__":
    downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/createCode.py","createCode.py")
    try:
        from createCode import *
    except:
        print("Run this program again.")
        quit()

    CHAR_LIST = []
    files = os.listdir()

    downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/defaultCode.json",'defaultCode.json')
    files = os.listdir()

    code = readCode()

    match input("Which do you want to do?\n Type enc for encoding.\n Type dec for decoding.\n"):
        case "enc":
            match input("On file or not?\n Write file or text."):
                case "file":
                    encodeFile(code,str(input("File path:")))
                    print("Done!")
                    quit()
                case "text":
                    print(encode(code,input("Text to encode:\n")))
                    quit()
                case _:
                    print("Invalid option.")
                    quit()
            print(encode(code,encode(code,input("Text to encode:\n"))))
            quit()
        case "dec":
            match input("On file or not?\n Write file or text."):
                case "file":
                    decodeFile(code,str(input("File path:")))
                    print("Done!")
                    quit()
                case "text":
                    print(code,decode(code,input("Text to decode:\n")))
                    quit()
                case _:
                    print("Invalid option.")
                    quit()      
        case _:
            print("Invalid option.")
