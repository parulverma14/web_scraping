import os
import json
import requests
from bs4 import BeautifulSoup


google_image="https://www.google.com/search?biw=1600&tbm=isch&source=hp&biw=&bih=783&ei=r8RAYLO4B-2Z4-EP1_S2uAw&"
user_agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
            }
'''url=urllib.request.urlopen(google_image)
html=url.read()
print(url.getcode())
print(html)
print(os.getcwd())
'''
os.chdir("C:\\Users\\Kunal\\Desktop")
print(os.getcwd())

Images_py="images" 
def folder_create ():
    if not os.path.exists(Images_py):
        os.mkdir(Images_py)
    download_images()
def download_images():
    data=input("What are you looking for :")
    no_images=int(input("How many images do you want :"))
    print (f"searching for {no_images} best images of {data}........")
    search_url = google_image +"q="+ data
    print(search_url)
    response=requests.get(search_url,headers=user_agent )
    html=response.text
    soup=BeautifulSoup(html,"html.parser")
    results=soup.find_all("img",{'class':'rg_i.Q4LuWd'}, limit=no_images)
    print(results)
    image_links = []
    for result in results:
        text = result.text
        print(text)
        text_dict=json.loads(text)
        link=text_dict['Q4LuWd']
        image_links.append(link)

    print(f'found {len(image_links)} images')
    x = len(image_links)
    if x == 0:
        print("CANT DOWNLOAD")
    else:
        print("start downloading....")

    for i , image_link in enumerate (image_links):
        response=requests.get(image_link)
        image_name=Images_py+"/"+data+str(i+1)+ ".jpg"
        with open(image_name,"wb")as file:
            file.write(response.content)
    print("DONE")
folder_create()
