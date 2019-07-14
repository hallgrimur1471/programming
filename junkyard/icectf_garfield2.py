#!/usr/bin/env python3.7

cipher = "IjgJUOPLOUVAIRUSGYQUTOLTDSKRFBTWNKCFT"
key = "07271978"
data = ""

for i in range(0, len(cipher)):
    data += chr(ord(cipher[i]) - int(key[i % len(key)]))

print(data)
print(key+key+key)


# cipher[i] - data[i] = key[i % len(key)]
# data[i] = cipher[i] - key[i % len(key)]

# IceCTF{I_DONT_:HINK_GRONSFELD_LIKE9_MONDA?S
