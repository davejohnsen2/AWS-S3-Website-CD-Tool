import threading
import boto3
import webbrowser
import os
from os import walk

#Customize these variables for your application
sitebaseurl = "https://Example.com" #Main site URL
bucketls = {".js": 'MYBUCKET/MYSUBFOLDERFORJSFILES',
          '.html':'MYBUCKET/MYSUBFOLDERFORHTMLFILES'} # list of file types and bucket where files should be uploaded
openchrome = True #True if you want the program to open the new file in google chrome

# Program initialization
dirname = os.path.dirname(__file__)
wfpath = os.path.join(dirname, '_webfiles')
wfpath = wfpath.replace("\\", "/")
lastfile, lastfiletime = [], []
fileup = {}
s3 = boto3.client('s3')

# Poll folder and subfolders and update AWS S3 if file is updated
def files_in_folder(path):
    for (dirpath, dirnames, filenames) in walk(path):
        break
    for files in filenames:
        for types in bucketls.keys():
            if os.path.splitext(files)[1] == types:
                if fileup.get(files) != os.path.getmtime(path+"/"+files):
                    if fileup.get(files) != None:
                        #  call to AWS code here
                        upAWSS3(path+"/"+files,files,types)
                    fileup[files] = os.path.getmtime(path+"/"+files)
                    break
    for dirs in dirnames:
        files_in_folder(path+"/"+dirs)
    return fileup

# Sends updated file to AWS S3 and then opens chrome if openchrome = true
def upAWSS3(filepath,filename,type):
    # Check for js or html to determine destination bucket
    bucketwfold = bucketls[type]
    bucket = bucketwfold.split("/")[0]  
    name = bucketwfold[bucketwfold.index("/")+1:] + "/" + filename
    
    # Send file to S3
    data = open(filepath, 'rb')
    s3.put_object(ACL='public-read',Bucket=bucket,Key=name, Body=data)
    print(bucket + "/" + name + " updated")
    
    # Open chrome to view update
    if openchrome:
        url = sitebaseurl+"/#!/"+os.path.splitext(filename)[0]
        webbrowser.open_new_tab(url)

# Poll folder and subfolders every x seconds
def setInterval(time):
    e = threading.Event()
    while not e.wait(time):
        files_in_folder(wfpath)

setInterval(0.5)
