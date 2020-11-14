import os
import time


os.system("hashcat.exe -m 1800 -a 0 -o salida50.txt --outfile-format=2  archivo_5 diccionario_2.dict")

print(time.clock())
