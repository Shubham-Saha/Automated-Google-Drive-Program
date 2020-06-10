#!/usr/bin/env python3
import pyAesCrypt
import os
from os import stat, remove
import csv

global new_name
enc_list = {}

def do_enc(item, password_enc, path):
    os.chdir(path)
    bufferSize = 64 * 1024

    input_file = item
    output_file = "{}.aes".format(item)

    try:
        with open(input_file, "rb") as fIn:
            with open(output_file, "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password_enc, bufferSize)
                #get encrypted file
            encFileSize = stat(output_file).st_size


            new_name = "{}.{}.aes".format(input_file, encFileSize)
            os.rename(output_file, new_name)
    except FileNotFoundError:
        pass

    return new_name
