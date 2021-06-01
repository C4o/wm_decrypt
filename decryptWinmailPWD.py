import base64

s = "{wm_crypt}your browser saved winMail pwd"

def wm_decrpt(crypt):

    result = ""
    asciiStr = ""
    decodeStr = base64.b64decode(crypt.split("{wm_crypt}")[1])
    #print(type(decodeStr))
    for ch in  decodeStr:
        #print(type(ch))
        asciiStr += str(ch)

    for i in range(0,len(asciiStr),6):
        result += chr((int(asciiStr[i:i+6][:3]) & 15) + ((int(asciiStr[i:i+6][-3:]) & 15) << 4))

    return result

print (wm_decrpt(s))