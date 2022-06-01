import requests
from bs4 import BeautifulSoup
import wget
import tarfile
import os
import os.path
import shutil
import colorama
from colorama import Fore, Style




def main():
    print("1 - Latest Version : "+CheckVersion(), end="\n")
    print("2 - Custom version : input", end="\n")

    input1 = input("Choose :")

    if input1 == "1":
        print("1- x64")
        print("2- arm64")
        input2 = input("Choose : ")
        if input2 == "1":
            DownloadAndExtractFile("x64")
        elif input2 == "2":
            DownloadAndExtractFile("arm64")
            pass
    elif input1 == "2":
        CheckVersion("1")
       
        pass

 #       r = requests.get(updatelink)
#        urllib.request.urlretrieve(updatelink, "asd.zip")

#        file = open("file/", 'wb')
#        for chunk in r.iter_content(100000):
#           file.write(chunk)
#        file.close()
#        pass
    print("Setup Succesfull")
    pass


def CheckVersion(version = None):
    if version == "1":
        r = requests.get("https://github.com/gitpod-io/openvscode-server/releases")
        soup = BeautifulSoup(r.text,'html.parser')

        for i in soup.find_all("h1"):
            print(i.text)
            pass
        pass
        return None
    try:
        r = requests.get("https://github.com/gitpod-io/openvscode-server/releases/latest/")
        soup = BeautifulSoup(r.text, 'html.parser')
        find = soup.find("h1")

        return find.text
    except:
        print("There was a problem with the network connection or the program.")

    pass


def DownloadAndExtractFile(cpu):
    path = CheckVersion()+"-linux-"+cpu+".tar.gz"
    updatelink = "https://github.com/gitpod-io/openvscode-server/releases/download/" +CheckVersion()+"/"+path
    wget.download(updatelink)
    print("\n")

    tar = tarfile.open(path)
    tar.extractall()
    tar.close()
    os.remove(path)
    if os.path.exists("vscodeweb-"+cpu+"/") == True:
       # os.removedirs("vscodeweb-"+cpu+"/")
        shutil.rmtree("vscodeweb-"+cpu+"/")
        pass
    os.rename(CheckVersion()+"-linux-"+cpu, "vscodeweb-"+cpu)
    pass

def Settings():
    
    pass


main()
