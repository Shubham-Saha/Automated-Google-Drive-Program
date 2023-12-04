# Automated-Google-Drive-Program

This is a basic security project for educational purposes.

# About the Program

In recent times, we are much more used to cloud storage to store our data. There are many cloud storage providers around the world. Their main purpose is to store our data and provide us with the data when we need it. 
The most widely used cloud storage is Google Drive. In our day-to-day work, we use it a lot. To use this we need to visit Google Drive’s website or navigate Google Drive’s application.

After this, we can upload, delete and download files from there. This is pretty much easy and flexible for users. The security of the data from the time of uploading and storing is provided by Google itself. In our daily lives, we might need to upload a bunch of files and download them too.
But if someone gets access to anyone’s Google Drive and steals the data while the owner of the data is not around? Google can’t do anything there to stop that unauthorized person. 
They have a feature, in which we can encrypt any of our files in the drive after uploading. But this requires a lot of time. Visiting the website or navigating apps then uploading or downloading files, encrypting files and then decrypting them seems very much manual work in a day to day life for a regular Google Drive user.

1. What if all of that work is done in a minimum amount of time?
2. What if the file is encrypted with AES256 while uploading it to the Drive automatically?
3. What if all the files, folders and files in folders are visible in a list?
4. What if the files are easily downloaded and then decrypted too?

All of these are possible using the Automated Google Drive Program. This program is Shell Scripted using Python.
The reason behind the shell is to minimize the user’s time. We know that visiting a website or using an application GUI takes a lot of time in backend processing whereas direct shell commands take less time to process.

This program is for those users who use Google Drive in their daily work and need to save a lot of time investing in Google Drive.

This is a cross-platform program. It means this program can run on different OS machines.

# How this program works

This program establishes a connection with Google Drive using Google Drive API and for authentication and authorization, OAuth 2.0 of Google is used.

After a successful authentication, the program starts. To know how the program is working in practice, a video is uploaded. It is recommended to read the whole documentation and satisfy the prerequisites before running the program and then watch the full video to learn how to operate this program.


# Prerequisites

To run this file below things are needed to be installed in the machine if they are not present.

1. Python 3.7 or above version. (Not below 3.7)

2. pip 20.1.1 https://pypi.org/project/pip/

3. google-auth-oauthlib 0.4.1 - https://pypi.org/project/google-auth-oauthlib/

4. google-api-python-client 1.9.2 https://pypi.org/project/google-api-python-client/

5. google-auth 1.16.1 https://pypi.org/project/google-auth/

6. PyDrive 1.3.1 https://pypi.org/project/PyDrive/

7. pickle5 0.0.10 https://pypi.org/project/pickle5/

8. pyAesCrypt 0.4.3 https://pypi.org/project/pyAesCrypt/

9. Google Client Library :

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib






# Exceptions in this program

While uploading files without encryption for the first an error may raise, something like this:

googleapiclient.errors.HttpError: <HttpError 400 when requesting 
https://www.googleapis.com/upload/drive/v2/files?
alt=json&uploadType=resumable returned "Bad Request">


raise ApiRequestError(error)
pydrive.files.ApiRequestError: <HttpError 400 when requesting 
https://www.googleapis.com/upload/drive/v2/files?
alt=json&uploadType=resumable returned "Bad Request">


Don’t panic. This just arises because of an API request which is an exception of Google Drive API. Just wait for some time and try again. Sooner or later it will work.


# Enjoy !!!!
