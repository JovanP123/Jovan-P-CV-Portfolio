chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}', ';', ':', "'", '"', '\\', '|', ',', '<', '.', '>', '/', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ', "nL", "lmbd"]
import random
#Generate, embed in txt file, and fetch keys from txt files
def generateKey():
    key = {}
    nums = []
    for i in range(len(chars)+6):
        if i<5:
            continue
        nums.append(i)
    for i in range(len(chars)):
        if len(nums)==1:
            key[nums[0]] = chars[i]
            break
        rndIt = random.randint(1,len(nums)-1)
        key[chars[i]] = nums[rndIt]
        nums.pop(rndIt)
    return key
def embedKey(kyFlLoc,key):
    kyFl = open(kyFlLoc,"w")
    keyNums = list(key.values())
    for i in range(len(key)):
        kyFl.write(str(keyNums[i])+"~"+str(chars[i])+"\n")
    kyFl.close()
    return 0
def fetchKey(kyFlLoc):
    kyFl = open(kyFlLoc,"r")
    kyCode = kyFl.read()
    kyPairs = kyCode.split("\n")
    kyPairs.pop(-1)
    key = {}
    for i in range(len(kyPairs)):
        splitPair = kyPairs[i].split("~")
        key[int(splitPair[0])] = splitPair[1]
    kyFl.close()
    return key
#Encrypting and decrypting data
def encryptTxtFile(filePath,newEncryptedFileLocation,fileName):
    encFit = open(newEncryptedFileLocation+"\\"+fileName+"RND"+".txt","w")
    encRnd = open(newEncryptedFileLocation+"\\"+fileName+"FIT"+".txt","w")
    encKey = open(newEncryptedFileLocation+"\\"+fileName+"KEY"+".txt","w")
    encKey.close()
    currentFile = open(filePath,"r")
    data = currentFile.read()
    key = generateKey()
    it = 0
    while it!=len(data):
        if data[it]!="~" and data[it]!="\n":
            rndInt = random.randint(1,key[data[it]]-1)
            encRnd.write(str(rndInt)+" ")
            encFit.write(str(key[data[it]]-rndInt)+" ")
        elif data[it]=="~":
            rndInt = random.randint(1,key["lmbd"])
            encRnd.write(str(rndInt)+" ")
            encFit.write(str(key["lmbd"]-rndInt)+" ")
        elif data[it]=='\n':
            rndInt = random.randint(1,key["nL"])
            encRnd.write(str(rndInt)+" ")
            encFit.write(str(key["nL"]-rndInt)+" ")
        it+=1
    currentFile.close()
    encFit.close()
    encRnd.close()
    embedKey(newEncryptedFileLocation+"\\"+fileName+"KEY"+".txt",key)
    print("Succesfully made encrypted copy of the txt file!")
def decryptTxtFile(rndFilePath,fitFilePath,keyFilePath):
    text = ""
    rnd = open(rndFilePath,"r")
    fit = open(fitFilePath,"r")
    keyFl = open(keyFilePath,"r")
    key = fetchKey(keyFilePath)
    rndString = rnd.read()
    fitString = fit.read()
    rndString = rndString.split(" ")
    fitString = fitString.split(" ")
    rndString.pop(-1)
    fitString.pop(-1)
    for i in range(len(rndString)):
        if key[int(rndString[i])+int(fitString[i])]=="nL":
            text += "\n"
        elif key[int(rndString[i])+int(fitString[i])]=="lmbd":
            text += "~"
        else: text += key[int(rndString[i])+int(fitString[i])]
    return print(text)
def extractEncryptedTxtFile(rndFilePath,fitFilePath,keyFilePath,newDecryptedFileLocation,newDecryptedFileName):
    text = ""
    rnd = open(rndFilePath,"r")
    fit = open(fitFilePath,"r")
    key = fetchKey(keyFilePath)
    rndString = rnd.read()
    fitString = fit.read()
    rndString = rndString.split(" ")
    fitString = fitString.split(" ")
    rndString.pop(-1)
    fitString.pop(-1)
    for i in range(len(rndString)):
        if key[int(rndString[i])+int(fitString[i])]=="nL":
            text += "\n"
        elif key[int(rndString[i])+int(fitString[i])]=="lmbd":
            text += "~"
        else: text += key[int(rndString[i])+int(fitString[i])]
    newFile = open(newDecryptedFileLocation+"\\"+newDecryptedFileName,"w")
    newFile.write(text)
    newFile.close()
    print("Succesfull data extraction")
def directEncrypt(data,keyLocation,keyName):
    encRnd = ""
    encFit = ""
    encKey = ""
    key = generateKey()
    embedKey(keyLocation+"\\"+keyName+".txt",key)
    it = 0
    while it!=len(data):
        if data[it]!="~" and data[it]!="\n":
            rndInt = random.randint(1,key[data[it]]-1)
            encRnd+=(str(rndInt)+" ")
            encFit+=(str(key[data[it]]-rndInt)+" ")
        elif data[it]=="~":
            rndInt = random.randint(1,key["lmbd"])
            encRnd+=(str(rndInt)+" ")
            encFit+=(str(key["lmbd"]-rndInt)+" ")
        elif data[it]=='\n':
            rndInt = random.randint(1,key["nL"])
            encRnd+=(str(rndInt)+" ")
            encFit+=(str(key["nL"]-rndInt)+" ")
        it+=1
    return ["RND:"+encRnd,"FIT:"+encFit,"KEY:"+keyLocation+"\\"+keyName+".txt"]
def directDecrypt(rndString,fitString,keyFileLocation):
    text = ""
    key = fetchKey(keyFileLocation)
    rndString = rndString.split(" ")
    fitString = fitString.split(" ")
    rndString.pop(-1)
    fitString.pop(-1)
    for i in range(len(rndString)):
        if key[int(rndString[i])+int(fitString[i])]=="nL":
            text += "\n"
        elif key[int(rndString[i])+int(fitString[i])]=="lmbd":
            text += "~"
        else: text += key[int(rndString[i])+int(fitString[i])]
    return print(text)
print("""---Welcome to the RND-FIT-KEY Text File Encryption Terminal---
The way this system works is that for every new encryption,
a key is generated. This key is a hash map(dictionary) that has numbers from
5 to 100 as keys, and all the letters/characters/symbols as values.
In the RND file, an array of numbers is generated, each one for each letter/symbol in the txt file.
But the range of randomness is from 1 to the number that letter was assigned in the
newly generated key, minus 1. So when this number is generated, the number in the same
position in the FIT file is placed, and that is the number that is needed for when you
add it to the RND number pair, it sums up to the number that the letter/symbol was assinged
to. After the data is encrypted, the data can't be decrypted without all three of the files. So if
the either one of the RND, FIT or KEY files is missing, the data cannot be decrypted.

Features:

encryptTxtFile~[txtFileLocation]~[newEncryptedFilesLocation]~[encryptedFileName]
|
V
Encrypts a txt file into RND-FIT-KEY encryption

decryptTxtFile~[rndTxtFileLocation]~[fitTxtFileLocation]~[keyTxtFileLocation]
|
V
Decrypts RND-FIT-KEY encryption files in the terminal

extractEncryptedTxtFile~[rndTxtFileLocation]~[fitTxtFileLocation]~[keyTxtFileLocation]~[newDecryptedFileLocation]~[newDecryptedFileName]
|
V
Extracts data from the encrypted file into a new txt file

EXIT
|
V
Exits file""")
terminal = [""]
splitTerminal = [""]
while splitTerminal[0]!="EXIT":
    terminal = input(">>>")
    splitTerminal = terminal.split("~")
    if splitTerminal[0]=="encryptTxtFile":
        encryptTxtFile(splitTerminal[1],splitTerminal[2],splitTerminal[3])
    elif splitTerminal[0]=="decryptTxtFile":
        decryptTxtFile(splitTerminal[1],splitTerminal[2],splitTerminal[3])
    elif splitTerminal[0]=="extractEncryptedTxtFile":
        extractEncryptedTxtFile(splitTerminal[1],splitTerminal[2],splitTerminal[3],splitTerminal[4],splitTerminal[5])
