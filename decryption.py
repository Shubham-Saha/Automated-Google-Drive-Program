#!/usr/bin/env python3
import pyAesCrypt
import os
from os import stat, remove
import re

encFileSize = 0

def do_dec(file_name, path, password_dec):
    try:
        os.chdir(path)
        bufferSize = 64 * 1024

        input_file = str(file_name)
        output_file = re.sub(r'(.[0-9]*.aes)', r'', input_file)
        encFile = re.search(r'[0-9]+', input_file)
        encFileSize = int(encFile[0])


        with open(input_file, "rb") as fIn:
            with open(output_file, "wb") as fOut:
                pyAesCrypt.decryptStream(fIn, fOut, password_dec, bufferSize, encFileSize)

    except FileNotFoundError:
        pass
    except TypeError:
        pass

    return output_file
