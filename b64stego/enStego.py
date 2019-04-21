import base64
import sys
def enStego(sourceFile,setgoFile,message):
    b64table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    with open(sourceFile,'r') as sourceText, open(setgoFile,'w') as setgoText:
        print(message)
        message = "".join([bin(ord(i))[2:].zfill(8) for i in message])
        for line in sourceText:
            text = base64.b64encode(line[:-1].encode("utf-8")).decode("utf-8")
            l = text.count('=')
            if 0 < 2*l <= len(message):                
                text = text[:-l-1] + b64table[b64table.index(text[-l-1])+int(message[:2*l],2)] + text[-l:]
                message = message[2*l:]
            setgoText.write(text+'\n')
            if not len(message):
                break
    return len(message)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        print("Remaining",enStego(sys.argv[1],sys.argv[2],sys.argv[3]),"bits!")
    else:
        print("Remaining",enStego("source.txt","stego.txt","SimpleMessage\n"),"bits!")
