import re
import os

archivo_out = os.path.join(os.getcwd(), 'preproinsulin-clean.txt')

texto=""
with open('preproinsulin-seq.txt') as f:
    texto = f.read()
    print(texto)
patron = r'(\d [0-9])'
cadenas = re.sub(patron, r'\1\n', texto)

texto =  texto[17:]
result = ''.join(i for i in texto if not i.isdigit())
result = result[:-2]
with open(archivo_out, 'w') as outfile:
    outfile.write(result)