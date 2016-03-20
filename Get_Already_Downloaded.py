import os
import urllib.request
def Manager(Links):
    Method = "Get_Already_Downloaded - Manager"
    Files = os.listdir(".")
    for Link in Links:
        try:
            filename = Link.split("/")[len(Link.split("/"))-1]
            if filename in Files:
                FileSize_Online = int(urllib.request.urlopen(Link).info()["Content-Length"])
                FileSize_OnDisk = int(os.path.getsize(filename))
                if FileSize_Online == FileSize_OnDisk:
                    print ("["+Link+"] Removed since it is already downloaded")
                    Links.remove(Link)
        except:
            print ("[[[ERROR]]] in "+Method)
    return Links
