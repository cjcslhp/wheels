import base64

def enStego(sourceFile,setgoFile,message):
    b64table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    with open(sourceFile,'r') as sourceText, open(setgoFile,'w') as setgoText:
        message = "".join([bin(ord(i))[2:].zfill(8) for i in message])
        print(message)
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

print("Remaining",enStego("source.txt","stego.txt","SimpleMessage\n"),"bits!")