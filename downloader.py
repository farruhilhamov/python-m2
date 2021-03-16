import requests

links = []
a = 1
while a == True:
    inp = input("enter url: ")
    if len(inp) >= 4:
        links.append(inp)
    elif inp == "":
        a = 0

def saver(link):
    filename = link.split('/') [-1]
    r =requests.get(link,allow_redirects = True)
    print(filename)
    
    with open(filename,'wb') as file:
        file.write(r.content)

    return filename
readylink = []

for z in links:
    readylink.append(saver(z))
    print(readylink)
