import urllib.request

def Manager(Links):
    Method = "Download_Files - Manager"
    Errors = []
    for Link in Links:
        try:
            LinkSep = Link.split("/")
            LinkLen = len(LinkSep)
            filename = LinkSep[LinkLen-1]
            print ("Downloading ["+filename+"]")
            urllib.request.urlretrieve(Link,filename)
        except:
            print ("[[[ERROR]]] in "+Method)
    print (Errors)
