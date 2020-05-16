import sys
import os
from github import Github
import time


path = "C:/Users/camil/OneDrive/Desktop/PythonProjects/"
username = "milosoria"
password = "tegustaelpico1"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))
    time.sleep(2)
if __name__ == "__main__":
    create()