import hashlib
import os
import time

file = open('salida5.txt', 'w')
with open('salida50.txt', 'r') as f:
    for linea in f:
        sha_signature= \
            hashlib.sha256(linea.encode()).hexdigest()
        file.write(sha_signature+ os.linesep)
file.close()
print(time.clock())
