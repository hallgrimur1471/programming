#!/usr/bin/env python3.7

cipher = "‡r‡n35‡h7‡o‡ca‡nq‡c‡k‡rv9‡xz‡wp"
with open("mess.txt", "r") as f:
    cipher = f.readlines()
cipher = cipher[0].rstrip()

with open("codecs_list.txt", "r") as f:
    encodings = f.readlines()
encodings = list(map(lambda e: e.strip(), encodings))

for encoding in encodings:
    try:
        print(f"trying encoding {encoding}")
        print(bytes(cipher, encoding="utf-8").decode(encoding))
    except (UnicodeDecodeError, LookupError):
        pass

#cipher = "‡r‡n35‡h7‡o‡ca‡nq‡c‡k‡rv9‡xz‡wp"
#for encoding in encodings:
#    try:
#        print(f"trying encoding {encoding}")
#        print(bytes(cipher, encoding=encoding))
#    except:
#        pass
#
