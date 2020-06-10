#!/usr/bin/env python3
from driveAPI import *
from fileProcess import *
import os
from encryption import *
from decryption import *
from version import *
from release import *
from dev_details import *

def scan_dir(dir_decision):
    if dir_decision == '1':
        print("-"*100)
        print("\n".join(drive_dir))
        print("-"*100)
    else:
        print("Enter the correct input: ")
        dir_decision = input()
        return scan_dir(dir_decision)

def enc_up(enc_decision):
    if enc_decision == 'Y' or enc_decision == 'y':
        start_process_with_enc()
        print("-"*100)
    elif enc_decision == 'N' or enc_decision == 'n':
        start_process_without_enc()
        print("-"*100)
    else:
        print("Enter the correct input.: ")
        dir_decision = input()
        return enc_up(enc_decision)


def start_process_with_enc():
    dir = os.listdir(path)
    print("Enter the password for encryption: ")
    password_enc = input()
    print("Please wait a while.....")
    for item in dir:
        if decision == "root":
            try:
                item = do_enc(item, password_enc, path)
                upload_file_to_DriveRoot(item, path)
                os.remove(item)
            except IsADirectoryError:
                pass
            except FileNotFoundError:
                pass
        else:
            try:
                fid = isfolder_exists(decision)
                item = do_enc(item, password_enc, path)
                upload_file_to_DriveFolder(item, fid, path)
                os.remove(item)
            except IsADirectoryError:
                pass
            except FileNotFoundError:
                pass

def start_process_without_enc():
    dir = os.listdir(path)
    print("Please wait a while.....")
    for item in dir:
        if decision == "root":
            try:
                upload_file_to_DriveRoot(item, path)
            except IsADirectoryError:
                pass
            except FileNotFoundError:
                pass
        else:
            try:
                fid = isfolder_exists(decision)
                upload_file_to_DriveFolder(item, fid, path)
            except IsADirectoryError:
                pass
            except FileNotFoundError:
                pass


def enc_down(file_name, path):
    try:
        os.chdir(path)
        dir= os.listdir(path)
        name = file_name
        with open('upload_list.csv') as files:
            reader = csv.reader(files)
            uploaded_files_list = dict(reader)

        if file_name in uploaded_files_list:
            file1 = drive.CreateFile({'id': uploaded_files_list[file_name]})
            res_file = file1.GetContentFile(file_name)
            print("File Downloaded.")
        else:
            print("No such file found. Try again.")
    except FileNotFoundError:
        print("upload_list.csv not found. Please place the csv file in the selected folder for downloading files.")

#os.system("taskkill /im firefox.exe /f")
print("-"*100)
print("Automated Google Drive Program.")
print("-"*100)
print("-"*100)
while True:
    print("-"*100)
    print("Choose your option:")
    print("Features: Press F")
    print("Version: Press V")
    print("Release Date: Press R")
    print("Developer Details: Press D")
    print("Exit: Press X")
    print("-"*100)

    pressed = input()

    if pressed == 'F' or pressed == 'f':
        print("-"*100)
        print("View full drive contents: Press 1")
        print("For uploading file: Press 2")
        print("To download file: Press 3")
        print("To decrypt file: Press 4")
        print("-"*100)
        pressed1 = input()
        if pressed1 == '1':
            scan_dir(pressed1)
        elif pressed1 == '2':
            print("-"*100)
            path = input("Insert the full path of the directory: ")
            print("-"*100)
            print("Where do you want to save your file?")
            print("Option 1: Type root to save file in root directory of drive.")
            print("Option 2: Type the folder name for specific folder.")
            print("Option 3: Type the folder name to create a new folder and save the file there.")
            print("-"*100)

            print("-"*100)
            decision = input()
            print("-"*100)
            print("Do you want to encrypt the files before uploading? Press Y/N")
            enc_decision = input()
            enc_up(enc_decision)
            print("-"*100)
            print("File Transfer Completed.")
            print("-"*100)
            print("-"*100)
            print("Uploaded files: ")
            print("\n".join(uploaded_files_list))
            print("-"*100)
        elif pressed1 == '3':
            print("-"*100)
            file_name = input("Enter the file name: ")
            path = input("Enter the path to save the file: ")
            print("Downloading...")
            print("-"*100)
            enc_down(file_name, path)
        elif pressed1 == '4':
            print("-"*100)
            input_name = input("Enter the file name: ")
            input_loc = input("Enter the path of the file: ")
            print("Enter the password for decryption: ")
            password_dec = input()
            print("-"*100)
            os.chdir(input_loc)
            dir = os.listdir(input_loc)
            for item in dir:
                if item == input_name:
                    try:
                        do_dec(input_name, input_loc, password_dec)
                        print("-"*100)
                        print("Decryption Completed.")
                        print("-"*100)
                        break
                    except ValueError:
                        print("Wrong Password.")


    elif pressed == 'V' or pressed == 'v':
        version()
    elif pressed == 'R' or pressed == 'r':
        release()
    elif pressed == 'D' or pressed == 'd':
        dev_details()
    elif pressed == 'X' or pressed == 'x':
        print("-"*100)
        print("Closing....")
        print("-"*100)
        break
    else:
        print("-"*100)
        print("Enter the right keyword.")
        print("-"*100)
