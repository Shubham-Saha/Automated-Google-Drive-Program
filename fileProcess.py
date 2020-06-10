#!/usr/bin/env python3
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import csv
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance.

def create_new_folder(folder_name):
    folder = drive.CreateFile({"title": folder_name, "mimeType": "application/vnd.google-apps.folder"})
    folder.Upload()
    return folder['id']

def isfolder_exists(folder_name):
    # Auto-iterate through all files in the root folder.
    folder_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for dfolder in folder_list:
        if dfolder['title'] == folder_name:
            return dfolder['id']
        else:
            folder_id = create_new_folder(folder_name)
            return folder_id

uploaded_files_list = {}
        
def upload_file_to_DriveRoot(title, path):
    # Create GoogleDriveFile instance
    file = drive.CreateFile({'title': title})
    file.SetContentFile(path + title)
    file.Upload()
    
    uploaded_files_list[file['title']] = file['id']
    os.chdir(path)
    with open("upload_list.csv", 'w+', newline='') as ufile:
        writer = csv.writer(ufile)
        for key, value in set(uploaded_files_list.items()):
            writer.writerow([key, value])
            
    return True



def upload_file_to_DriveFolder(title, fid, path):
    file = drive.CreateFile({"title": title, "parents": [{"kind": "drive#fileLink", "id": fid}]})
    file.SetContentFile(path + title)
    file.Upload()

    uploaded_files_list[file['title']] = file['id']
    os.chdir(path)
    with open("upload_list.csv", 'w+', newline='') as ufile:
        writer = csv.writer(ufile)
        for key, value in set(uploaded_files_list.items()):
            writer.writerow([key, value])

    return True
