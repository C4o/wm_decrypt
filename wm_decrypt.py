# created in 20191120

import base64

s = "{wm_crypt}pIelhqOHpIetgqGDooOjgw=="

def wm_decrpt(crypt):

	result = ""
	asciiStr = ""
	decodeStr = base64.b64decode(crypt.split("{wm_crypt}")[1])

	for i in range(0, len(decodeStr), 1):
		asciiStr += str(ord(decodeStr[i]))

	for i in range(0,len(asciiStr),6):
		result += chr((int(asciiStr[i:i+6][:3]) & 15) + ((int(asciiStr[i:i+6][-3:]) & 15) << 4))

	return result

print wm_decrpt(s)
