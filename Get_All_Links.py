import urllib.request
from bs4 import BeautifulSoup

def Manager(coreURL):
    PageObject = {"Links":[],
              "More Pages":True}
    PageNum = 1
    while PageObject["More Pages"]:
        URL = coreURL+str(PageNum)
        content = Read_Page(URL)
        PageObject = Scrape_Page(content,PageObject)
        PageNum+=1
    return PageObject["Links"]
def Read_Page(URL):
    print ("Enter Read_Page")
    with urllib.request.urlopen(URL) as webpage:
        content = webpage.read()
    BS4content = BeautifulSoup(content,"html.parser")
    return BS4content
def Scrape_Page(content,PageObject):
    localHrefs = []
    print ("Enter Scrape_Page")
    #Check if there are more pages
    Page_Selector_Area = content.find(class_="pagination")
    ul = Page_Selector_Area.find('ul')
    lis = ul.find_all('li')
    if "disabled" in str(lis[len(lis)-1]):
        PageObject["More Pages"] = False
    #Get local hrefs
    container = content.find(class_="container")
    downloads = container.find_all(class_="download")
    for download in downloads:
        a = download.find("a")
        a['href'] = a['href'][1:]
        localHrefs.append(a['href'])
    for localHref in localHrefs:
        modal = content.find(id=localHref)
        modalbody = modal.find(class_="modal-body")
        lis = modalbody.find_all("li")
        for li in lis:
            if "Download (Mirror)" in str(li):
                a = li.find("a")
                PageObject["Links"].append(a['href'])
    return PageObject



